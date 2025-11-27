# Steam Games Database

База данных приложений Steam в формате JSON. Содержит AppID и названия приложений из Steam Store.

> - Важная информация
> - Данные собраны из баз 2023-2024 годов
> - Возможно присутствие удаленных приложений/игр
> - Не гарантируется полнота списка
> - Некоторые записи могут содержать пустые названия

Статистика
- Всего приложений: 184,479
- Обновлено: 2025-11-28
- Формат: JSON
- Источники: Базы данных 2023-2024 годов

Файлы

- `games.json` - Основная база (отсортирована по AppID)
- `games_minified.json` - Минифицированная версия (для production)
- `games_by_name.json` - Версия отсортированная по названиям
- `metadata.json` - Метаданные и статистика базы

Быстрый старт

```python
import json

# Загрузка данных
with open('games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)

# Получение названия по AppID
def get_game_name(appid):
    return games.get(str(appid), "Game not found")

print(get_game_name("730"))  # Counter-Strike: Global Offensive

# Поиск по названию (регистронезависимый)
def search_games(query):
    query = query.lower()
    return {appid: name for appid, name in games.items() 
            if query in name.lower()}

# Поиск всех игр Counter-Strike
cs_games = search_games("counter-strike")
