from utils.helpers import color_text, add_vertical_spaces
from db.shop_db import shop_data
from db.db_functions import reload_player_data


def ask_go_shopping():
    valid_inputs = ["yes", "no"]
    print(color_text("Would you like to go shopping?", "magenta"))
    print(color_text("Enter Yes or No:", "yellow"))
    while True:
        shopping_input = input().strip().lower()
        if shopping_input in valid_inputs:
            return shopping_input == "yes"


def ask_which_shop():
    player_data = reload_player_data()
    available_shops: list[str] = shop_data[player_data["current_realm"]].keys()

    for shop in available_shops:
        print(color_text(shop.title(), "cyan"))
    add_vertical_spaces(1)
    print(color_text("Which shop would you like to visit?", "yellow"))
    print(color_text('Or enter "Back" to change your mind', "yellow"))
    add_vertical_spaces(1)
    while True:
        shop_input = input().strip().lower()
        if shop_input == "back":
            return "back"
        elif shop_input in available_shops:
            return shop_input


def go_to_shop(shop_choice: str):
    print(shop_choice)
