db_file_path = "db/db.py"

def clear_db():
    new_content = "player_data = {}\n"

    with open(db_file_path, "w") as db_file:
        db_file.write(new_content)


def save_player_data(player_save: dict):
    new_content = f"player_data = {player_save}\n"

    with open(db_file_path, "w") as db_file:
        db_file.write(new_content)
    
    print("Player Data Saved Successfully!")
