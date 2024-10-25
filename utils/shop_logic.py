from utils.helpers import (
    color_text,
    add_vertical_spaces,
    press_space_to_continue,
    reset_screen,
)
from db.shop_db import shop_data
from db.item_db import item_data
from db.db_functions import reload_player_data, save_player_data


def print_current_funds():
    player_data = reload_player_data()
    print(
        color_text(f"You currently have {player_data['current_funds']} gold", "yellow")
    )
    add_vertical_spaces(1)


def print_details(item: dict, is_weapon=False):
    print(color_text(item["name"], "cyan", "underline"))
    print(color_text(item["description"], "blue"))
    if is_weapon:
        print(color_text(f'Base Damage: {item["base_damage"]}', "red"))
    print(color_text(f'Cost: {item["base_price"]} Gold', "yellow"))
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
    available_shops = shop_data[player_data["current_realm"]].keys()

    while True:
        reset_screen()
        print_current_funds()
        print_available_shops(list(available_shops))

        shop_input = input().strip().lower()
        if shop_input == "back":
            return
        elif shop_input in available_shops:
            if go_to_shop(shop_input) == "back":
                continue


def go_to_shop(shop_choice: str):
    player_data = reload_player_data()
    current_shop = shop_data[player_data["current_realm"]][shop_choice]
    current_items = current_shop["items"]

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

        shop_action = input().strip().lower()
        if shop_action == "back":
            return "back"

        elif shop_action == "buy":
            handle_buying(current_items)

        elif shop_action == "sell":
            handle_selling()


def handle_buying(current_items):
    player_data = reload_player_data()
    plural_class = {
        "archer": "archers",
        "swordsman": "swordsmen",
        "magician": "magicians",
    }

    while True:
        purchasable_items, purchasable_item_names = [], []

        reset_screen()
        print_current_funds()

        if isinstance(current_items, dict):  # Weapon shop
            print(
                color_text(
                    f"Here are the weapons available to {plural_class[player_data['weapon_class']]}:",
                    "magenta",
                )
            )
            add_vertical_spaces(1)
            current_weapons = current_items["weapons"][player_data["weapon_class"]]
            for weapon in current_weapons:
                print_details(weapon, is_weapon=True)
                purchasable_items.append(weapon)
                purchasable_item_names.append(weapon["name"].lower())

            print(color_text("We also sell:", "magenta"))
            add_vertical_spaces(1)
            if "other" in current_items:
                for other in current_items["other"]:
                    print_details(other)
                    purchasable_items.append(other)
                    purchasable_item_names.append(other["name"].lower())

        else:  # General shop
            print(color_text("Here is what we have in stock:", "magenta"))
            add_vertical_spaces(1)
            for item in current_items:
                print_details(item)
                purchasable_items.append(item)
                purchasable_item_names.append(item["name"].lower())

        print(color_text("What would you like to buy?", "yellow"))
        print(color_text('Or enter "Back" to change your mind', "yellow"))
        add_vertical_spaces(1)

        purchase_input = input().strip().lower()
        if purchase_input == "back":
            break
        elif purchase_input in purchasable_item_names:
            purchase_item(
                purchasable_items[purchasable_item_names.index(purchase_input)],
            )


def purchase_item(item: dict):
    player_data = reload_player_data()
    reset_screen()
    #
    print(item)
    #
    if player_data["current_funds"] < item["base_price"]:
        print(color_text("You don't have the funds for that item!", "red", "underline"))
        press_space_to_continue()
    else:
        while True:
            print_current_funds()
            print(
                color_text(
                    f"Are you sure you want to buy the {item['name']} for {item['base_price']} Gold?",
                    "cyan",
                )
            )
            print(color_text("Enter Yes or No:", "yellow"))
            add_vertical_spaces(1)

            confirm_purchase = input().strip().lower()
            if confirm_purchase in ["yes", "no"]:
                if confirm_purchase == "yes":
                    reset_screen()
                    player_data["current_funds"] -= item["base_price"]
                    print(color_text(f"You purchased the {item['name']}!", "green"))
                    add_vertical_spaces(1)
                    press_space_to_continue()
                    #! If they just bought a weapon
                    if item["category"] == "weapons":
                        while True:
                            reset_screen()
                            print(
                                color_text(
                                    "You cannot wield 2 weapons at once, though...",
                                    "red",
                                )
                            )
                            add_vertical_spaces(1)
                            print(
                                color_text(
                                    f"Would you like to sell your {player_data['current_weapon']['name']} for {player_data['current_weapon']['resell_price']} Gold or store it for later?"
                                )
                            )
                            print(color_text('Enter "Sell It" or "Store It":'))
                            old_weapon_input = input().strip().lower()
                            if old_weapon_input in ["sell it", "store it"]:
                                reset_screen()
                                if old_weapon_input == "store it":
                                    player_data["stored_weapons"].append(
                                        player_data["current_weapon"]
                                    )
                                    print(
                                        color_text(
                                            f"You had your previous weapon stored and equipped the {item['name']}!",
                                            "blue",
                                        )
                                    )
                                else:
                                    player_data["current_funds"] += player_data[
                                        "current_weapon"
                                    ]["resell_price"]
                                    print(
                                        color_text(
                                            f"You sold your previous weapon and equipped the {item['name']}!",
                                            "blue",
                                        )
                                    )
                                player_data["current_weapon"] = item
                                save_player_data(player_data)
                                add_vertical_spaces(1)
                                press_space_to_continue()
                                return
                    #! If they just bought anything else
                    else:
                        player_data["item_inventory"].append(item["name"].lower())
                        save_player_data(player_data)
                        return

                break


def handle_selling():
    player_data = reload_player_data()
    stored_weapons: list[dict] = player_data["stored_weapons"]
    item_inventory: list[str] = player_data["item_inventory"]
    sellable_weapons = []

    while True:
        reset_screen()
        print(color_text("Here are your stored weapons:", "magenta"))
        for weapon in stored_weapons:
            print(color_text(weapon["name"], "cyan", "underline"))
            print(color_text(weapon["description"], "blue"))
            print(
                color_text(f'Can be sold for: {weapon["resell_price"]} Gold', "yellow")
            )
            sellable_weapons.append(weapon["name"].lower())
            add_vertical_spaces(1)
        print(color_text("Here are the items in your inventory:", "magenta"))
        for item in item_inventory:
            if item in item_data["quest_items"]:
                item_dict = item_data["quest_items"][item]
            if item in item_data["heal_items"]:
                item_dict = item_data["heal_items"][item]
            if item in item_data["buff_items"]:
                item_dict = item_data["buff_items"][item]
            if item in item_data["battle_items"]:
                item_dict = item_data["battle_items"][item]
            print(
                f'{color_text(item_dict["name"], "cyan", "underline")} => {color_text(item_dict["description"], "blue")}'
            )
            print(
                color_text(
                    f'Can be sold for: {item_dict["resell_price"]} Gold', "yellow"
                )
            )
            add_vertical_spaces(1)
        print(color_text("What would you like to sell?", "green"))
        print(color_text('Or enter "Back" to change your mind', "yellow"))
        sell_input = input().strip().lower()
        if sell_input == "back":
            return
        if sell_input in sellable_weapons:
            print("you tryna sell a weapon")
            press_space_to_continue()
            break

        if sell_input in item_inventory:
            print("you tryna sell an item")
            press_space_to_continue()
            break
