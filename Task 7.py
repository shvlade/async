import concurrent.futures
import time
import random


def process_data(item):
    """
    Обрабатывает элемент данных (имитация CPU-bound операции)
    """
    process_time = random.uniform(0.5, 2.0)
    time.sleep(process_time)
    result = item * 2  # простая операция
    print(f"Обработан элемент {item} -> {result} (время: {process_time:.2f}с)")
    return result


def run_pool(data, workers):
    """
    Запускает обработку данных в пуле потоков
    """
    print(f"\nЗапуск ThreadPoolExecutor с {workers} потоками")
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(process_data, data))

    total_time = time.time() - start
    print(f"Время выполнения: {total_time:.2f} сек\n")
    return total_time, results


def task7_thread_pool():
    data = list(range(1, 11))
    print("ОБРАБОТКА ДАННЫХ С ПОМОЩЬЮ ПУЛА ПОТОКОВ")


    time_2, results_2 = run_pool(data, workers=2)


    time_4, results_4 = run_pool(data, workers=4)


    time_8, results_8 = run_pool(data, workers=8)

    print("\nСРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print(f"Пул 2 потоков: {time_2:.2f} сек")
    print(f"Пул 4 потоков: {time_4:.2f} сек")
    print(f"Пул 8 потоков: {time_8:.2f} сек")

    print("\nРЕЗУЛЬТАТЫ ОБРАБОТКИ")
    print("Пул 2 потоков:", results_2)
    print("Пул 4 потоков:", results_4)
    print("Пул 8 потоков:", results_8)


# task7_thread_pool()
task7_thread_pool()
