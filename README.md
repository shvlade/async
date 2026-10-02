# HTTP: sync vs async

> Сравнение последовательных и асинхронных HTTP-запросов: requests, asyncio, aiohttp, семафор и измерение времени.

**Стек:** Python · asyncio · aiohttp · requests

## Что сравнивается

Один и тот же набор из 100 URL JSONPlaceholder обрабатывается последовательно через `requests` и конкурентно через `aiohttp`. Скрипт печатает длительность обоих запусков и их отношение.

- Ограничение конкурентности через `asyncio.Semaphore` (в демонстрации — 50).
- Повторное использование `aiohttp.ClientSession`.
- Таймауты и логирование ошибок.
- Сбор результатов через `asyncio.gather`.

## Запуск

```bash
git clone https://github.com/shvlade/async.git
cd async
python -m pip install aiohttp requests
python main.py
```

Для демонстрации нужен интернет. Измеренное ускорение зависит от сети, сервера и числа одновременных запросов; при ошибках в результат добавляется пустой словарь. Счётчик записей отражает длину списка, а не число успешных запросов.

## Основные функции

| Функция | Назначение |
| --- | --- |
| `fetch_sync(urls)` | Последовательные запросы |
| `fetch_url(session, url, semaphore)` | Один асинхронный запрос |
| `main_async(urls, concurrent_limit)` | Ограничение конкурентности и сбор результатов |

---

[← Профиль и другие проекты](https://github.com/shvlade) · [Каталог проектов](https://github.com/shvlade/shvlade/blob/main/PROJECTS.md)
