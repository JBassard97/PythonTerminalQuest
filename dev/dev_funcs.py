from utils.helpers import reset_screen, add_vertical_spaces, clear_terminal
from db.db_functions import save_player_data, reload_player_data


def print_player_data_all(player_data: dict):
    for items in player_data.items():
        print(items)


def dev_options(player_data: dict):
    reset_screen()
    while True:
        print("DEV PORTAL")
        add_vertical_spaces(2)

        dev_choices = ["view player_data", "change player_data", "total wipe", "exit"]
        for choice in dev_choices:
            print(choice)
        add_vertical_spaces(2)

        dev_input = input("What would you like to do?\n\n").strip().lower()

        #! Add dev functions here
        if dev_input == "view player_data":
            reset_screen()
            print_player_data_all(player_data)
        elif dev_input == "exit":
            reset_screen()
            break  # This will exit the while loop and stop the infinite loop.
        else:
            continue

        add_vertical_spaces(2)
        continue_input = input('Continue "dev" or "play"?\n\n').strip().lower()

        if continue_input == "dev":
            reset_screen()
        elif continue_input == "play":
            clear_terminal()
            break  # Exits the function to return to the game
