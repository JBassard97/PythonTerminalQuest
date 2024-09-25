import importlib
import db.player_db as player_db

player_db_file_path = "db/player_db.py"


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
