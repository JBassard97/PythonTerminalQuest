from db.db_functions import reload_player_data, reload_battle_data, clear_battle_db
from db.item_db import item_data
from utils.helpers import color_text, add_vertical_spaces


def ask_player_choice():
    player_options = f'{color_text("- Attack -", "red")} {color_text("- Defend -", "blue")} {color_text("- Use Item -", "green")} {color_text("- Run Away -", "yellow")}'

    valid_player_choices = [
        "attack",
        "defend",
        "use item",
        "run away",
    ]
    print(player_options)
    print(color_text("               What will you do?", "cyan"))

    while True:

        player_choice = input("                    ").strip().lower()

        if player_choice in valid_player_choices:
            return player_choice


def ask_attack_who():
    enemy_stats = reload_battle_data()
    first_enemy_display_name: str = enemy_stats[0]["display_name"]
    print(f'{color_text("          Who will be attacked?", "cyan")}')
    add_vertical_spaces(1)
    if enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]:
        print(
            f'{color_text(f"{first_enemy_display_name}", "red")} {color_text("A", "yellow")} {color_text("or", "cyan")} {color_text("B?", "yellow")}'
        )
        print(color_text("Enter A or B", "cyan"))
        valid_target_choices = ["a", "b"]
    else:
        second_enemy_display_name: str = enemy_stats[1]["display_name"]

        print(
            f'{color_text(f"{first_enemy_display_name}", "red")} {color_text("or", "cyan")} {color_text(f"{second_enemy_display_name}?", "red")}'
        )
        valid_target_choices = [
            first_enemy_display_name.lower(),
            second_enemy_display_name.lower(),
        ]
    add_vertical_spaces(1)
    while True:
        target_choice = input().strip().lower()
        if target_choice in valid_target_choices:
            if enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]:
                return target_choice
            elif target_choice == valid_target_choices[0]:
                return first_enemy_display_name
            elif target_choice == valid_target_choices[1]:
                return second_enemy_display_name


def ask_which_item():
    player_data = reload_player_data()
    for item in player_data["item_inventory"]:
        if item in item_data["heal_items"]:
            print(
                f'{color_text(item, "green")} => {color_text(item_data["heal_items"][item]["description"], "green")}'
            )
        elif item in item_data["quest_items"]:
            pass  # ? Quest items not intended for battle use
        elif item in item_data["buff_items"]:
            print(
                f'{color_text(item, "blue")} => {color_text(item_data["buff_items"][item]["description"], "blue")}'
            )
        elif item in item_data["battle_items"]:
            print(
                f'{color_text(item, "red")} => {color_text(item_data["battle_items"][item]["description"], "red")}'
            )
    valid_item_choices = player_data["item_inventory"]
    add_vertical_spaces(1)
    print(
        color_text(
            "Which item will you use? (enter 'Back' to change your mind)",
            "cyan",
        )
    )
    while True:
        item_choice = input("     ").strip().lower()
        if item_choice == "back":
            return "back"
        elif item_choice in valid_item_choices:
            return item_choice


def ask_use_item_on_who(
    item_choice: str,
):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()
    if len(enemy_stats) == 1 and item_choice in item_data["battle_items"]:
        return enemy_stats[0]["display_name"]  # Only one enemy, so no need to ask
    if item_choice in item_data["heal_items"]:
        print(
            f'{color_text(item_choice, "green")} => {color_text(item_data["heal_items"][item_choice]["description"], "green")}'
        )
    elif item_choice in item_data["buff_items"]:
        print(
            f'{color_text(item_choice, "blue")} => {color_text(item_data["buff_items"][item_choice]["description"], "blue")}'
        )
    elif item_choice in item_data["battle_items"]:
        print(
            f'{color_text(item_choice, "red")} => {color_text(item_data["battle_items"][item_choice]["description"], "red")}'
        )
    add_vertical_spaces(1)

    print(color_text("Who will you use the " + item_choice + " on?", "cyan"))
    if item_choice in item_data["heal_items"] or item_choice in item_data["buff_items"]:
        print(
            f'{color_text(player_data["name"], player_data["color"])} {color_text("or", "yellow")} {color_text(player_data["companion_name"] + "?", player_data["color"])}'
        )
        add_vertical_spaces(1)
        formal_protags_to_fight: list[str] = [
            player_data["name"],
            player_data["companion_name"],
        ]
        valid_item_targets = [item.lower() for item in formal_protags_to_fight]
        while True:
            item_target_choice = input().strip().lower()
            if item_target_choice in valid_item_targets:
                if item_target_choice == valid_item_targets[0]:
                    return player_data["name"]
                else:
                    return player_data["companion_name"]
    elif item_choice in item_data["battle_items"]:
        if len(enemy_stats) == 2:
            if enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]:
                print(
                    f'{color_text(enemy_stats[0]["display_name"] + " A", "red")} {color_text("or", "yellow")} {color_text("B?", "red")}'
                )
                print(color_text("Enter: A or B", "yellow"))
                valid_item_targets = ["a", "b"]
            else:
                formal_enemies_to_fight: list[str] = [
                    enemy_stats[0]["display_name"],
                    enemy_stats[1]["display_name"],
                ]
                print(
                    f'{color_text(f"{formal_enemies_to_fight[0]}", "red")} {color_text("or", "yellow")} {color_text(f"{formal_enemies_to_fight[1]}?", "red")}'
                )
                valid_item_targets = [item.lower() for item in formal_enemies_to_fight]
        add_vertical_spaces(1)
        while True:
            item_target_choice = input().strip().lower()
            if item_target_choice in valid_item_targets:
                if item_target_choice == valid_item_targets[0]:
                    return formal_enemies_to_fight[0]
                else:
                    return formal_enemies_to_fight[1]


def ask_companion_choice():
    player_data = reload_player_data()
    companion_options = f'{color_text("- Attack -", "red")} {color_text("- Defend -", "blue")} {color_text("- Love You -", "green")}'
    valid_companion_choices = ["attack", "defend", "love you"]
    print(companion_options)
    print(color_text(f"     What will {player_data['companion_name']} do?", "cyan"))
    while True:
        companion_choice = input("            ").strip().lower()
        if companion_choice in valid_companion_choices:
            return companion_choice
