#!/usr/bin/env python3
"""
Скрипт для проверки целостности данных
"""

import json

def validate_data():
    """Проверяет данные на проблемы"""
    
    print("🔍 Проверка целостности данных...")
    
    with open('data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)
    
    print(f"📊 Всего записей: {len(games)}")
    
    # Статистика
    appids = [int(k) for k in games.keys() if k.isdigit()]
    if appids:
        print(f"📈 Диапазон AppID: {min(appids)} - {max(appids)}")
    
    # Примеры
    print(f"\n🔍 Примеры записей (первые 5):")
    for i, (appid, name) in enumerate(list(games.items())[:5]):
        print(f"   {appid}: {name}")

if __name__ == "__main__":
    validate_data()