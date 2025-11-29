import asyncio
import time
from datetime import datetime


async def scheduled_task(name, priority, duration):
    """
    Асинхронная задача с приоритетом и временем выполнения
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Задача '{name}' (приоритет {priority}) начата")
    await asyncio.sleep(duration)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Задача '{name}' завершена")
    return f"Результат {name}"


async def task6_async_scheduler():
    """
    Асинхронный планировщик:
    - Задачи сортируются по приоритету
    - Одновременно исполняются не более 2 задач
    - Выводится порядок завершения
    """
    tasks_with_priority = [
        ("Экстренная задача", 1, 1),
        ("Важная задача", 2, 2),
        ("Обычная задача A", 3, 3),
        ("Обычная задача B", 3, 2),
        ("Фоновая задача", 4, 5)
    ]

    print("\nСортировка задач по приоритету")
    sorted_tasks = sorted(tasks_with_priority, key=lambda x: x[1])
    for t in sorted_tasks:
        print(f"Задача '{t[0]}' (приоритет {t[1]}, длительность {t[2]} сек)")

    semaphore = asyncio.Semaphore(2)  # Ограничиваем параллельность до 2 задач
    results = []

    async def sem_task(name, priority, duration):
        async with semaphore:
            return await scheduled_task(name, priority, duration)

    # Создаем корутины по приоритету
    coroutines = [
        sem_task(name, priority, duration)
        for name, priority, duration in sorted_tasks
    ]

    print("\n Запуск задач ")
    results = await asyncio.gather(*coroutines)

    print("\n Порядок завершения ")
    for r in results:
        print(r)

    print("\nВсе задачи завершены!")


# Запуск
asyncio.run(task6_async_scheduler())
