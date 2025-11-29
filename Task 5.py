import time
import threading
import multiprocessing
import asyncio
from concurrent.futures import ProcessPoolExecutor


def io_task(name, duration):
    time.sleep(duration)
    return f"{name} completed"


async def async_io_task(name, duration):
    await asyncio.sleep(duration)
    return f"{name} completed"


def io_task_unpack(args):
    name, duration = args
    return io_task(name, duration)


def run_async(tasks):
    async def main():
        coros = [async_io_task(name, duration) for name, duration in tasks]
        return await asyncio.gather(*coros)
    return asyncio.run(main())


def task5_performance_comparison():
    tasks = [("Task1", 2), ("Task2", 3), ("Task3", 1), ("Task4", 2), ("Task5", 1)]

    #СИНХРОННО
    print("СИНХРОННО")
    start = time.time()
    sync_results = [io_task(name, duration) for name, duration in tasks]
    sync_time = time.time() - start
    print(sync_results, f"{sync_time:.2f} сек")

    #ПОТОКИ
    print("\nМНОГОПОТОЧНО")
    start = time.time()
    thread_results = []

    def thread_worker(name, duration):
        thread_results.append(io_task(name, duration))

    threads = []
    for name, duration in tasks:
        t = threading.Thread(target=thread_worker, args=(name, duration))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    thread_time = time.time() - start
    print(thread_results, f"{thread_time:.2f} сек")

    # ПРОЦЕССЫ
    print("\nМНОГОПРОЦЕССНО")
    start = time.time()

    with ProcessPoolExecutor() as executor:
        process_results = list(executor.map(io_task_unpack, tasks))

    process_time = time.time() - start
    print(process_results, f"{process_time:.2f} сек")

    #АСИНХРОННО
    print("\nАСИНХРОННО")
    start = time.time()
    async_results = run_async(tasks)
    async_time = time.time() - start
    print(async_results, f"{async_time:.2f} сек")

    #АНАЛИЗ
    print("\n АНАЛИЗ")
    print(f"Синхронно:      {sync_time:.2f} сек")
    print(f"Потоки:         {thread_time:.2f} сек")
    print(f"Процессы:       {process_time:.2f} сек")
    print(f"Асинхронно:     {async_time:.2f} сек")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    task5_performance_comparison()
