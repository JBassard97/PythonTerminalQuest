from assets.battle_ascii_sprites import print_battle_sprites_side_by_side
from utils.helpers import color_text, reset_screen, add_vertical_spaces
from db.enemy_db import enemy_data
from db.item_db import item_data
import random


#! 1 or 2 randomly selected enemies to fight
def random_enemy_count():
    return random.choice([1, 2])


def create_enemies_to_fight(enemy_possibilities: list):
    enemies_to_fight: list[str] = []
    for i in range(random_enemy_count()):
        enemies_to_fight.append(random.choice(enemy_possibilities))

    return enemies_to_fight


#! Creating enemy description string
def create_enemy_string(enemies_to_fight: list[str], player_data: dict):
    enemy_string = ""
    if len(enemies_to_fight) == 2:  # If there are 2 enemies...
        if enemies_to_fight[0] == enemies_to_fight[1]:  # And they're the same enemy...
            duplicate_enemy = enemies_to_fight[0]
            enemy_string = f"                                2 {enemy_data[player_data['current_realm']][duplicate_enemy]['display_name']}s"
        else:  # 2 enemies and they're different...
            enemy_string = f"                                  {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']} and {enemy_data[player_data['current_realm']][enemies_to_fight[1]]['display_name']}"
    else:  # There's just one enemy...
        enemy_string = f"          {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']}"

    return enemy_string


#! Creating protag description string
def create_protag_string(protags_to_fight: list[str], player_data: dict):
    protag_string = ""
    if len(protags_to_fight) == 2:
        protag_string = f"{player_data['name']} and {player_data['companion_name']}"
    else:
        protag_string = player_data["name"]

    return protag_string


#! Prints "Enemies VS Protags" on top of battle
def print_battle_desc(enemy_string: str, protag_string: str, player_data: dict):
    desc_string = f'{color_text(enemy_string, "red")} {color_text("VS", "cyan")} {color_text(protag_string, player_data["color"])}{color_text("!!!", "cyan")}'
    print(desc_string)


#! Displaying the battle
def display_battle(
    enemy_string: str,
    protag_string: str,
    player_data: dict,
    enemies_to_fight: list[str],
    protags_to_fight: list[str],
):
    reset_screen()
    print_battle_desc(enemy_string, protag_string, player_data)
    add_vertical_spaces(1)
    print_battle_sprites_side_by_side(
        enemies_to_fight, "red", protags_to_fight, player_data["color"]
    )
    add_vertical_spaces(1)
    print(color_text(player_data["name"] + "'s stats:", player_data["color"]))
    print(
        f'Health: {player_data["player_current_health"]}/{player_data["player_max_health"]} | Attack: {player_data["current_attack"]} | Defense: {player_data["current_defense"]} | Speed: {player_data["current_speed"]}'
    )
    add_vertical_spaces(1)
    if player_data["is_companion_alive"]:
        print(
            color_text(
                player_data["companion_name"] + "'s stats:", player_data["color"]
            )
        )
        print(
            f'Health: {player_data["companion_current_health"]}/{player_data["companion_max_health"]} | Attack: {player_data["companion_current_attack"]} | Defense: {player_data["companion_current_defense"]} | Speed: {player_data["companion_current_speed"]}'
        )
        add_vertical_spaces(1)


#! ---------- BEGIN COMPLEX BATTLE QUESTIONS -------------


def ask_player_choice():
    player_options = f'{color_text("- Attack -", "red")} {color_text("- Defend -", "blue")} {color_text("- Use Item -", "green")} {color_text("- Run Away -", "yellow")}'

    valid_player_choices = ["attack", "defend", "use item", "run away"]
    print(player_options)
    print(color_text("               What will you do?", "cyan"))

    while True:

        player_choice = input("                    ").strip().lower()

        if player_choice in valid_player_choices:
            return player_choice


def ask_attack_who(enemies_to_fight: list, player_data: dict):
    first_enemy_display_name: str = enemy_data[player_data["current_realm"]][
        enemies_to_fight[0]
    ]["display_name"]
    print(f'{color_text("          Who will you attack?", "cyan")}')
    add_vertical_spaces(1)
    if enemies_to_fight[0] == enemies_to_fight[1]:
        print(
            f'{color_text(f"{first_enemy_display_name}", "red")} {color_text("A", "yellow")} {color_text("or", "cyan")} {color_text("B?", "yellow")}'
        )
        print(color_text("Enter A or B", "cyan"))
        valid_target_choices = ["a", "b"]
    else:
        second_enemy_display_name: str = enemy_data[player_data["current_realm"]][
            enemies_to_fight[1]
        ]["display_name"]
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
            return target_choice


def ask_which_item(player_data: dict):
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
    enemies_to_fight: list[str],
    player_data: dict,
):
    if len(enemies_to_fight) == 1 and item_choice in item_data["battle_items"]:
        return enemies_to_fight[0]  # Only one enemy, so no need to ask
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
        if len(enemies_to_fight) == 2:
            if enemies_to_fight[0] == enemies_to_fight[1]:
                print(
                    f'{color_text(enemy_data[player_data["current_realm"]][enemies_to_fight[0]]["display_name"] + " A", "red")} {color_text("or", "yellow")} {color_text("B?", "red")}'
                )
                print(color_text("Enter: A or B", "yellow"))
                valid_item_targets = ["a", "b"]
            else:
                formal_enemies_to_fight: list[str] = [
                    enemy_data[player_data["current_realm"]][enemies_to_fight[0]][
                        "display_name"
                    ],
                    enemy_data[player_data["current_realm"]][enemies_to_fight[1]][
                        "display_name"
                    ],
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


def ask_companion_choice(player_data: dict):
    companion_options = f'{color_text("- Attack -", "red")} {color_text("- Defend -", "blue")} {color_text("- Love You -", "green")}'
    valid_companion_choices = ["attack", "defend", "love you"]
    print(companion_options)
    print(color_text(f"     What will {player_data['companion_name']} do?", "cyan"))
    while True:
        companion_choice = input("            ").strip().lower()
        if companion_choice in valid_companion_choices:
            return companion_choice

    #! ---------- BEGIN BATTLE LOGIC -------------------------


def battle_play_by_play(
    player_choice: str,
    companion_choice: str = None,  # ? If None, companion is dead
    player_attack_target: str = None,  # ? If None, player isn't attacking
    item_choice: str = None,  # ? If None, player isn't using an item
    item_target_choice: str = None,  # ? If None, item target is implied or isn't using an item
):

    #! Handle player_choice
    print("you will " + player_choice)
    #! Handle companion_choice
    if companion_choice is not None:
        print("your companion will " + companion_choice)
    else:
        print("your companion is dead, RIP")
    #! Handle player_attack_target
    if player_attack_target is not None:
        print("your attack targets " + player_attack_target)
    #! Handle item_choice
    if item_choice is not None:
        print("you will use " + item_choice)
    #! Handle item_target_choice
    if item_target_choice is not None:
        print(item_choice + " will be used on " + item_target_choice)
