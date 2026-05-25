import asyncio
import aiohttp
import requests
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_sync(urls: list[str]) -> list[dict]:
    results = []

    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            response.raise_for_status()
            results.append(response.json())

        except requests.RequestException as e:
            logging.error(f"Ошибка при запросе {url}: {e}")
            results.append({})

    return results


async def fetch_url(
    session: aiohttp.ClientSession,
    url: str,
    semaphore: asyncio.Semaphore
) -> dict:

    async with semaphore:
        try:
            timeout = aiohttp.ClientTimeout(total=3)

            async with session.get(url, timeout=timeout) as response:
                response.raise_for_status()
                return await response.json()

        except aiohttp.ClientError as e:
            logging.error(f"Ошибка сети при запросе {url}: {e}")
            return {}

        except asyncio.TimeoutError:
            logging.warning(f"Таймаут при запросе {url}")
            return {}


async def main_async(
    urls: list[str],
    concurrent_limit: int = 50
) -> list[dict]:

    semaphore = asyncio.Semaphore(concurrent_limit)

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_url(session, url, semaphore)
            for url in urls
        ]

        results = await asyncio.gather(*tasks)
        return results


if __name__ == "__main__":

    urls = [
        f"https://jsonplaceholder.typicode.com/comments/{i}"
        for i in range(1, 101)
    ]

    print("Синхронная версия")

    start_sync = time.time()
    sync_data = fetch_sync(urls)
    end_sync = time.time()

    sync_time = end_sync - start_sync

    print(f"Получено записей: {len(sync_data)}")
    print(f"Время выполнения: {sync_time:.2f} сек.")

    print()

    print("Асинхронная версия")

    start_async = time.time()
    async_data = asyncio.run(main_async(urls, concurrent_limit=50))
    end_async = time.time()

    async_time = end_async - start_async

    print(f"Получено записей: {len(async_data)}")
    print(f"Время выполнения: {async_time:.2f} сек.")

    print()

    print("Сравнение")

    if async_time > 0:
        print(f"Ускорение: {sync_time / async_time:.2f}x")