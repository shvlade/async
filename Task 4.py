import asyncio
import aiohttp
import time


async def fetch_url(session, url, name):
    """
    Асинхронно загружает веб-страницу
    """
    print(f"Начало загрузки {name}")

    try:
        async with session.get(url) as response:
            content = await response.text()
            print(f"Завершена загрузка {name}, статус: {response.status}")
            return len(content)
    except Exception as e:
        print(f"Ошибка при загрузке {name}: {e}")
        return 0


async def task4_async_scraper():
    """
    Задача: Создайте асинхронный веб-скрапер.

    URL для сканирования:
    1. "https://httpbin.org/delay/1" - "Сайт 1"
    2. "https://httpbin.org/delay/2" - "Сайт 2"
    3. "https://httpbin.org/delay/1" - "Сайт 3"
    4. "https://httpbin.org/delay/3" - "Сайт 4"

    Требуется:
    - Реализовать асинхронную загрузку всех URL
    - Использовать aiohttp для HTTP запросов
    - Измерить общее время выполнения
    - Вывести размер загруженного контента для каждого сайта
    """
    urls = [
        ("https://httpbin.org/delay/1", "Сайт 1"),
        ("https://httpbin.org/delay/2", "Сайт 2"),
        ("https://httpbin.org/delay/1", "Сайт 3"),
        ("https://httpbin.org/delay/3", "Сайт 4")
    ]

    start_time = time.time()

    # Ваш код здесь
    session = aiohttp.ClientSession()

    try:
        # Создаем задачи
        tasks = []
        for url, name in urls:
            tasks.append(fetch_url(session, url, name))

        # Выполняем все задачи
        results = await asyncio.gather(*tasks)

    finally:
        await session.close()

    # TODO: Создайте ClientSession
    # TODO: Создайте задачи для каждого URL
    # TODO: Используйте asyncio.gather для параллельного выполнения

    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} секунд")
    print(f"Размеры контента: {results}")

# Запуск задачи
# asyncio.run(task4_async_scraper())
asyncio.run(task4_async_scraper())