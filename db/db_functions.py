import importlib
import db.player_db as player_db
import db.battle_db as battle_db

player_db_file_path = "db/player_db.py"
battle_db_file_path = "db/battle_db.py"

# ! PLAYER_DB FUNCTIONS

def clear_player_db():
    new_content = "player_data = {}\n"

    with open(player_db_file_path, "w") as db_file:
        db_file.write(new_content)


def save_player_data(player_save: dict):
    new_content = f"player_data = {player_save}\n"

    with open(player_db_file_path, "w") as db_file:
        db_file.write(new_content)


def reload_player_data():
    importlib.reload(player_db)
    return player_db.player_data

# ! BATTLE_DB FUNCTIONS

def save_battle_data(enemies_to_fight: list[dict]):
    new_content = f"battle_data = {enemies_to_fight}\n"

    with open(battle_db_file_path, "w") as db_file:
        db_file.write(new_content)


def reload_battle_data():
    importlib.reload(battle_db)
    return battle_db.battle_data
