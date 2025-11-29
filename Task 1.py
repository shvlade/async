import time


def sync_calculate(operation, a, b, delay):
    """
    Выполняет математическую операцию с задержкой

    Параметры:
    operation (str): тип операции ('+', '-', '*', '/')
    a, b (float): числа для операции
    delay (float): время имитации вычислений

    Возвращает:
    float: результат операции
    """
    print(f"Начало операции {a} {operation} {b}")
    time.sleep(delay)  # Имитация долгого вычисления

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b if b != 0 else 'Ошибка: деление на ноль'
    else:
        result = 'Неизвестная операция'

    print(f"Конец операции {a} {operation} {b} = {result}")
    return result

def task1_sync_calculations():
    start_time = time.time()
    results = []
    # 1
    result1 = sync_calculate('+', 15, 25, 2)
    results.append(result1)
    # 2
    result2 = sync_calculate('-', 40, 18, 1)
    results.append(result2)
    # 3
    result3 = sync_calculate('*',12,8,3)
    results.append(result3)
    # 4
    result4 = sync_calculate('/', 100, 5, 1)
    results.append(result4)
    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} секунд")
    print(f"Результаты: {results}")

# Запуск задачи
# task1_sync_calculations()
task1_sync_calculations()