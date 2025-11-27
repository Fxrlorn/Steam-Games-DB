#!/usr/bin/env python3
"""
Создание различных версий базы данных
"""

import json
from datetime import datetime

def create_database_variants():
    """Создает разные версии базы данных"""
    
    print("🔄 Создание вариантов базы данных...")
    
    # Загрузка основной базы
    with open('data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)
    
    print(f"📊 Загружено записей: {len(games)}")
    
    # 1. Минифицированная версия
    with open('data/games_minified.json', 'w', encoding='utf-8') as f:
        json.dump(games, f, separators=(',', ':'), ensure_ascii=False)
    print("✅ Создан games_minified.json")
    
    # 2. Версия отсортированная по названиям
    sorted_by_name = dict(sorted(games.items(), key=lambda x: str(x[1]).lower()))
    with open('data/games_by_name.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_by_name, f, ensure_ascii=False, indent=2)
    print("✅ Создан games_by_name.json")
    
    # 3. Обновление метаданных
    update_metadata(games)
    
    print("\n🎯 Варианты базы данных созданы:")
    print(f"   📁 games.json ({len(games)} записей)")
    print(f"   📁 games_minified.json (минифицированная)")
    print(f"   📁 games_by_name.json (отсортировано по названиям)")

def update_metadata(games):
    """Обновляет метаданные базы"""
    
    # Подсчет статистики
    empty_names = sum(1 for name in games.values() if not str(name).strip())
    
    # Получаем AppID как числа для статистики
    appids = []
    for appid_str in games.keys():
        try:
            appids.append(int(appid_str))
        except ValueError:
            continue
    
    metadata = {
        "version": "1.0.0",
        "total_apps": len(games),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "data_sources": [
            "Steam Store API 2023",
            "Various game databases 2023-2024"
        ],
        "notes": [
            "Data collected from 2023-2024 sources",
            "May include delisted/removed applications",
            "List completeness is not guaranteed",
            "Some entries may have empty names"
        ],
        "statistics": {
            "total_entries": len(games),
            "empty_names": empty_names,
            "min_appid": min(appids) if appids else 0,
            "max_appid": max(appids) if appids else 0
        },
        "formats_available": [
            "games.json - Sorted by AppID",
            "games_minified.json - Minified version", 
            "games_by_name.json - Sorted by name"
        ]
    }
    
    with open('data/metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print("📊 Метаданные обновлены")

if __name__ == "__main__":
    create_database_variants()