# Steam Games Database

Complete database of Steam games and applications with AppID mapping. Contains 184,479 entries from 2023-2024 sources.

> ⚠️ **Important Note**
> - Data collected from 2023-2024 sources
> - May include delisted/removed applications  
> - List completeness is not guaranteed
> - Some entries may have empty names

## 📊 Statistics
- **Total applications**: 184,479
- **Last updated**: 2025-11-28
- **Format**: JSON
- **Sources**: 2023-2024 databases

## 🗂️ Files

- `data/games.json` - Main database (sorted by AppID)
- `data/games_minified.json` - Minified version for production
- `data/games_by_name.json` - Sorted by game names
- `data/metadata.json` - Database metadata and statistics

## 🚀 Quick Start

```python
import json

# Load database
with open('data/games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)

# Get game name by AppID
game_name = games.get("730")
print(game_name)  # Counter-Strike: Global Offensive

# Search games by name
def search_games(query):
    query = query.lower()
    return {appid: name for appid, name in games.items() 
            if query in name.lower()}

cs_games = search_games("counter-strike")
