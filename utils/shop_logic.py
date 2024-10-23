from utils.helpers import (
    color_text,
    add_vertical_spaces,
    press_space_to_continue,
    reset_screen,
)
from db.shop_db import shop_data
from db.db_functions import reload_player_data


def print_current_funds():
    player_data = reload_player_data()
    print(
        color_text(f"You currently have {player_data['current_funds']} gold", "yellow")
    )
    add_vertical_spaces(1)


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

    while True:
        reset_screen()
        print_current_funds()
        print(color_text("Available Shops:", "blue"))
        for shop in available_shops:
            print(color_text(shop.title(), "cyan"))
        add_vertical_spaces(1)
        print(color_text("Which shop would you like to visit?", "yellow"))
        print(color_text('Or enter "Back" to change your mind', "yellow"))
        add_vertical_spaces(1)
        shop_input = input().strip().lower()
        if shop_input == "back":
            return
        elif shop_input in available_shops:
            shop_outcome = go_to_shop(shop_input)
            if shop_outcome == "back":
                continue


def go_to_shop(shop_choice: str):
    valid_choices = ["buy", "sell", "back"]

    while True:
        reset_screen()
        print(
            color_text(
                f"Welcome to the {shop_choice.title()}! What can we do for you?", "cyan"
            )
        )
        add_vertical_spaces(1)
        for choice in valid_choices:
            print(color_text(choice.capitalize(), "green"))
        add_vertical_spaces(1)
        shop_action: str = input().strip().lower()
        if shop_action in valid_choices:
            if shop_action == "back":
                return "back"

            elif shop_action == "buy":
                reset_screen()
                print_current_funds()
                print("what are you buying?")
                press_space_to_continue()

            elif shop_action == "sell":
                reset_screen()
                print_current_funds()
                print("what are you selling?")
                press_space_to_continue()
