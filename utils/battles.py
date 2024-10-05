from db.enemy_db import enemy_data
from db.item_db import item_data
from utils.helpers import (
    reset_screen,
    add_vertical_spaces,
    color_text,
    press_space_to_continue,
)
from assets.battle_ascii_sprites import print_battle_sprites_side_by_side
import random


def ask_player_choice():
    player_options = f'{color_text("- Attack -", "red")} {color_text("- Defend -", "blue")} {color_text("- Use Item -", "green")} {color_text("- Run Away -", "yellow")}'

    valid_player_choices = ["attack", "defend", "use item", "run away"]
    print(player_options)
    print(color_text("               What will you do?", "cyan"))

    while True:

        player_choice = input("                    ").strip().lower()

        if player_choice in valid_player_choices:
            return player_choice


def start_random_battle(player_data: dict):
    #! 1 or 2 randomly selected enemies to fight
    def random_enemy_count():
        return random.choice([1, 2])

    # List of possible enemies for the realm the player is in
    enemy_possibilities = list(enemy_data[player_data["current_realm"]])
    enemies_to_fight = []
    for i in range(random_enemy_count()):
        enemies_to_fight.append(random.choice(enemy_possibilities))

    #! Creating enemy description string
    enemy_string = ""
    if len(enemies_to_fight) == 2:  # If there are 2 enemies...
        if enemies_to_fight[0] == enemies_to_fight[1]:  # And they're the same enemy...
            duplicate_enemy = enemies_to_fight[0]
            enemy_string = f"                                2 {enemy_data[player_data['current_realm']][duplicate_enemy]['display_name']}s"
        else:  # 2 enemies and they're different...
            enemy_string = f"                                  {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']} and {enemy_data[player_data['current_realm']][enemies_to_fight[1]]['display_name']}"
    else:  # There's just one enemy...
        enemy_string = f"          {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']}"

    #! Creating protagonist list (omitting companion if dead)
    protags_to_fight = [player_data["weapon_class"]]
    if player_data["is_companion_alive"]:
        protags_to_fight.append(player_data["companion_type"])

    #! Creating protag description string
    protag_string = ""
    if len(protags_to_fight) == 2:
        protag_string = f"{player_data['name']} and {player_data['companion_name']}"
    else:
        protag_string = player_data["name"]

    def print_battle_desc(enemy_string: str, protag_string: str):
        desc_string = f'{color_text(enemy_string, "red")} {color_text("VS", "cyan")} {color_text(protag_string, player_data["color"])}{color_text("!!!", "cyan")}'
        print(desc_string)

    #! Displaying the battle
    def display_battle(
        enemy_string: str, protag_string: str, player_data: dict, enemies_to_fight: list
    ):

        reset_screen()
        print_battle_desc(enemy_string, protag_string)
        add_vertical_spaces(1)
        print_battle_sprites_side_by_side(
            enemies_to_fight, "red", protags_to_fight, player_data["color"]
        )
        add_vertical_spaces(1)
        print(color_text(player_data["name"] + "'s stats:", player_data["color"]))
        print(
            f'Health: {player_data["player_current_health"]}/{player_data["player_max_health"]}'
        )
        print(
            f'Attack: {player_data["current_attack"]} | Defense: {player_data["current_defense"]} | Speed: {player_data["current_speed"]}'
        )
        add_vertical_spaces(1)
        if player_data["is_companion_alive"]:
            print(
                color_text(
                    player_data["companion_name"] + "'s stats:", player_data["color"]
                )
            )
            print(
                f'Health: {player_data["companion_current_health"]}/{player_data["companion_max_health"]}'
            )
            print(
                f'Attack: {player_data["companion_current_attack"]} | Defense: {player_data["companion_current_defense"]} | Speed: {player_data["companion_current_speed"]}'
            )
            add_vertical_spaces(1)

    def ask_attack_who(enemies_to_fight: list, player_data: dict):
        first_enemy_display_name: str = enemy_data[player_data["current_realm"]][
            enemies_to_fight[0]
        ]["display_name"]

        display_battle(enemy_string, protag_string, player_data, enemies_to_fight)

        print(f'{color_text("          Who will you attack?", "cyan")}')
        add_vertical_spaces(1)
        if enemies_to_fight[0] == enemies_to_fight[1]:
            print(
                f'{color_text(f"{first_enemy_display_name}", "red")} {color_text("A", "yellow")} {color_text(" or ", "cyan")} {color_text("B?", "yellow")}'
            )
            print(color_text("Enter A or B", "cyan"))
            valid_target_choices = ["a", "b"]
        else:
            second_enemy_display_name: str = enemy_data[player_data["current_realm"]][
                enemies_to_fight[1]
            ]["display_name"]
            print(
                f'{color_text(f"{first_enemy_display_name}", "red")} {color_text(" or ", "cyan")} {color_text(f"{second_enemy_display_name}?", "red")}'
            )
            valid_target_choices = [
                first_enemy_display_name.lower(),
                second_enemy_display_name.lower(),
            ]

        add_vertical_spaces(1)
        while True:
            target_choice = input()
            if target_choice in valid_target_choices:
                return target_choice

    def ask_which_item(player_data: dict):
        display_battle(enemy_string, protag_string, player_data, enemies_to_fight)
        for item in player_data["item_inventory"]:
            if item in item_data["heal_items"]:
                print(
                    f'{color_text(item, "green")} => {color_text(item_data["heal_items"][item]["description"], "green")}'
                )
            elif item in item_data["quest_items"]:
                print(
                    f'{color_text(item, "magenta")} => {color_text(item_data["quest_items"][item]["description"], "magenta")}'
                )
            elif item in item_data["buff_items"]:
                print(
                    f'{color_text(item, "blue")} => {color_text(item_data["buff_items"][item]["description"], "blue")}'
                )
            elif item in item_data["battle_items"]:
                print(
                    f'{color_text(item, "red")} => {color_text(item_data["battle_items"][item]["description"], "blue")}'
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

    def ask_companion_choice(player_data: dict):
        display_battle(enemy_string, protag_string, player_data, enemies_to_fight)

        companion_options = f'{color_text("- Attack -", "red")} {color_text("- Defend -", "blue")} {color_text("- Love You -", "green")}'
        valid_companion_choices = ["attack", "defend", "love you"]

        print(companion_options)
        print(color_text(f"     What will {player_data['companion_name']} do?", "cyan"))

        while True:

            companion_choice = input("            ").strip().lower()

            if companion_choice in valid_companion_choices:
                return companion_choice

    def ask_battle_questions(enemies_to_fight: list, player_data: dict):
        while True:
            display_battle(enemy_string, protag_string, player_data, enemies_to_fight)

            # Reset previous choices before asking again
            player_attack_target = None
            item_choice = None

            player_choice = ask_player_choice()

            if player_choice == "attack":
                if len(enemies_to_fight) == 2:
                    player_attack_target = ask_attack_who(enemies_to_fight, player_data)
                else:
                    player_attack_target = enemies_to_fight[0]

            elif player_choice == "defend":
                # Defend logic placeholder
                pass

            elif player_choice == "use item":
                item_choice = ask_which_item(player_data)

                # If player chose to go back, restart question loop
                if item_choice == "back":
                    continue

            elif player_choice == "run away":
                return  # Handle run away logic

            # Companion move (if companion is alive)
            if player_data["is_companion_alive"]:
                companion_choice = ask_companion_choice(player_data)
            else:
                companion_choice = None

            # Proceed to battle actions
            battle_play_by_play(
                player_choice, companion_choice, player_attack_target, item_choice
            )
            break  # Exit after resolving actions

    def battle_play_by_play(
        player_choice: str,
        companion_choice: str = None,  # ? If None, companion is dead
        player_attack_target: str = None,  # ? If None, player isn't attacking
        item_choice: str = None,  # ? If None, player isn't using an item
    ):
        #! Handle player_choice
        print("you will " + player_choice)
        #! Handle companion_choice
        if companion_choice is not None:
            print("your companion will " + companion_choice)
        #! Handle player_attack_target
        if player_attack_target is not None:
            print("your attack targets " + player_attack_target)
        #! Handle item_choice
        if item_choice is not None:
            print("you will use " + item_choice)

    ask_battle_questions(enemies_to_fight, player_data)


# def start_boss_battle(player_data: dict):
#     print("BOSS BATTLE")
