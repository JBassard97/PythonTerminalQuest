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


def print_available_shops(available_shops: list[str]):
    print(color_text("Available Shops:", "blue", "underline"))
    add_vertical_spaces(1)
    for shop in available_shops:
        print(color_text(shop.title(), "cyan"))
    add_vertical_spaces(1)
    print(color_text("Which shop would you like to visit?", "yellow"))
    print(color_text('Or enter "Back" to change your mind', "yellow"))
    add_vertical_spaces(1)


def print_weapon_details(weapon: dict):
    print(color_text(weapon["name"], "cyan", "underline"))
    print(color_text(weapon["description"], "blue"))
    print(color_text(f'Base Damage: {weapon["base_damage"]}', "red"))
    print(color_text(f'Cost: {weapon["base_price"]} Gold', "yellow"))
    add_vertical_spaces(1)


def print_item_details(item: dict):
    print(color_text(item["name"], "cyan", "underline"))
    print(color_text(item["description"], "blue"))
    print(color_text(f'Cost: {item["base_price"]} Gold', "yellow"))
    add_vertical_spaces(1)


def ask_go_shopping():
    valid_inputs = ["yes", "no"]
    print_current_funds()
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
        print_available_shops(available_shops)

        shop_input = input().strip().lower()
        if shop_input == "back":
            return
        elif shop_input in available_shops:
            shop_outcome = go_to_shop(shop_input)
            if shop_outcome == "back":
                continue


def go_to_shop(shop_choice: str):
    player_data = reload_player_data()
    current_shop: dict = shop_data[player_data["current_realm"]][shop_choice]
    current_items = current_shop["items"]

    valid_choices = ["buy", "sell", "back"]

    while True:
        player_data = reload_player_data()
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
                while True:
                    purchasable_items = []
                    purchasable_item_names = []

                    reset_screen()
                    print_current_funds()

                    if isinstance(
                        current_items, dict
                    ):  #! If it's a dict, then it's a weapon shop
                        plural_class = {
                            "archer": "archers",
                            "swordsman": "swordsmen",
                            "magician": "magicians",
                        }
                        print(
                            color_text(
                                f"Here are the weapons specifically available to {plural_class[player_data['weapon_class']]}:",
                                "magenta",
                            )
                        )
                        add_vertical_spaces(1)
                        current_weapons = current_items["weapons"][
                            player_data["weapon_class"]
                        ]
                        for weapon in current_weapons:
                            print_weapon_details(weapon)
                            purchasable_items.append(weapon)
                            purchasable_item_names.append(weapon["name"].lower())

                        print(color_text("We also sell:", "magenta"))
                        add_vertical_spaces(1)
                        if "other" in current_items.keys():
                            current_others = current_items["other"]
                            for other in current_others:
                                print_item_details(other)
                                purchasable_items.append(other)
                                purchasable_item_names.append(other["name"].lower())

                    else:  #! If it's not a dict, it's any other shop
                        print(color_text("Here is what we have in stock:", "magenta"))
                        for item in current_items:
                            print_item_details(item)
                            purchasable_items.append(item)
                            purchasable_item_names.append(item["name"].lower())

                    print(color_text("What would you like to buy?", "yellow"))
                    print(color_text('Or enter "Back" to change your mind', "yellow"))
                    add_vertical_spaces(1)
                    purchase_input = input().strip().lower()
                    if purchase_input == "back":
                        break
                    elif purchase_input in purchasable_item_names:
                        purchase_index = purchasable_item_names.index(purchase_input)
                        purchase_dict = purchasable_items[purchase_index]
                        reset_screen()
                        if player_data["current_funds"] < purchase_dict["base_price"]:
                            print(
                                color_text(
                                    "You don't have the funds for that item!",
                                    "red",
                                    "underline",
                                )
                            )
                            press_space_to_continue()
                            break
                        else:
                            while True:
                                print_current_funds()
                                print(
                                    color_text(
                                        f"Are you sure you want to buy the {purchase_dict['name']} for {purchase_dict['base_price']} Gold?",
                                        "cyan",
                                    )
                                )
                                print(color_text("Enter Yes or No:", "yellow"))
                                add_vertical_spaces(1)
                                valid_responses = ["yes", "no"]
                                confirm_purchase = input().strip().lower()
                                if confirm_purchase in valid_responses:
                                    if confirm_purchase == "yes":
                                        print("you gonna buy the thing")
                                        press_space_to_continue()
                                        break
                                    else:
                                        break

            elif shop_action == "sell":
                pass
                # reset_screen()
                # print_current_funds()
                # print("what are you selling?")
                # press_space_to_continue()
