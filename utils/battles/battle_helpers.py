from assets.battle_ascii_sprites import print_battle_sprites_side_by_side
from utils.helpers import (
    color_text,
    reset_screen,
    add_vertical_spaces,
    press_space_to_continue,
)
from db.db_functions import (
    save_battle_data,
    reload_battle_data,
    save_player_data,
    reload_player_data,
)
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


def random_enemy_move():
    move_possibilities = ["attack", "defend"]
    return random.choice(move_possibilities)


def random_enemy_attack_target(player_data: dict):
    target_possibilities = [player_data["name"]]
    if player_data["is_companion_alive"]:
        target_possibilities.append(player_data["companion_name"])
    return random.choice(target_possibilities)


def random_companion_attack_target(player_data: dict, enemy_stats: list[dict]):
    if enemy_stats[0] == enemy_stats[1]:
        target_possibilities = ["a", "b"]
        return random.choice(target_possibilities)
    else:
        target_possibilities = enemy_stats
        return random.choice(target_possibilities)["display_name"]


def move_index_to_word(index: int):
    dict = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    return dict[index + 1]  # + 1 because index starts at 0


#! Creating enemy description string
def create_enemy_string(enemies_to_fight: list[str], player_data: dict):
    enemy_string = ""
    if len(enemies_to_fight) == 2:  # If there are 2 enemies...
        if enemies_to_fight[0] == enemies_to_fight[1]:  # And they're the same enemy...
            duplicate_enemy = enemies_to_fight[0]
            enemy_string = f"                           2 {enemy_data[player_data['current_realm']][duplicate_enemy]['display_name']}s"
        else:  # 2 enemies and they're different...
            enemy_string = f"                             {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']} and {enemy_data[player_data['current_realm']][enemies_to_fight[1]]['display_name']}"
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
            if enemies_to_fight[0] == enemies_to_fight[1]:
                return target_choice
            elif target_choice == valid_target_choices[0]:
                return first_enemy_display_name
            elif target_choice == valid_target_choices[1]:
                return second_enemy_display_name


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


def ask_battle_questions(
    enemies_to_fight: list, player_data: dict, display_battle_params
):
    while True:
        display_battle(*display_battle_params)
        # Reset previous choices before asking again
        player_attack_target = None
        item_choice = None
        item_target_choice = None
        companion_choice = None
        player_choice = ask_player_choice()

        if player_choice == "run away":
            return "ran away"

        if player_choice == "attack":
            if len(enemies_to_fight) == 2:
                display_battle(*display_battle_params)
                player_attack_target = ask_attack_who(enemies_to_fight, player_data)
            else:
                player_attack_target = enemy_data[player_data["current_realm"]][
                    enemies_to_fight[0]
                ]["display_name"]
        elif player_choice == "defend":
            # Defend question placeholder
            pass
        elif player_choice == "use item":
            display_battle(*display_battle_params)
            item_choice = ask_which_item(player_data)
            # If player chose to go back, restart question loop
            if item_choice == "back":
                continue
            if (
                item_choice in item_data["heal_items"]
                or item_choice in item_data["buff_items"]
            ):
                if player_data["is_companion_alive"]:
                    display_battle(*display_battle_params)
                    item_target_choice = ask_use_item_on_who(
                        item_choice, enemies_to_fight, player_data
                    )
                else:
                    item_target_choice = player_data["name"]
            if item_choice in item_data["battle_items"]:
                if len(enemies_to_fight) == 2:
                    display_battle(*display_battle_params)
                    item_target_choice = ask_use_item_on_who(
                        item_choice, enemies_to_fight, player_data
                    )
                else:
                    item_target_choice = enemy_data[player_data["current_realm"]][
                        enemies_to_fight[0]
                    ]["display_name"]
        # Companion move (if companion is alive)
        if player_data["is_companion_alive"]:
            display_battle(*display_battle_params)
            companion_choice = ask_companion_choice(player_data)
        break

    display_battle(*display_battle_params)
    # Proceed to battle actions

    battle_outcome = battle_play_by_play(
        player_data,
        enemies_to_fight,
        display_battle_params,  # ? Gets passed in so that they can be used in ask_battle_questions again
        player_choice,
        companion_choice,
        player_attack_target,
        item_choice,
        item_target_choice,
    )
    # if battle_outcome == "ran away" or battle_outcome is None:
    #     return "ran away"  # Exit on "ran away"
    if battle_outcome:
        return battle_outcome


#! ---------- BEGIN BATTLE LOGIC -------------------------


def create_enemies_battle_stats(player_data: dict, enemies_to_fight: list[str]):
    enemy_battle_stats = []

    for enemy in enemies_to_fight:
        enemy = enemy_data[player_data["current_realm"]][enemy]
        enemy_battle_stats.append(enemy)

    return enemy_battle_stats


# ? Sorts all_fighters by "speed" stat
def create_battle_move_order(player_data: dict, enemy_stats: list[dict]):
    all_fighters = [
        {"player_name": player_data["name"], "speed": player_data["current_speed"]}
    ]
    if player_data["is_companion_alive"]:
        all_fighters.append(
            {
                "companion_name": player_data["companion_name"],
                "speed": player_data["companion_current_speed"],
            }
        )
    for enemy in enemy_stats:
        all_fighters.append(enemy)

    move_order = sorted(all_fighters, key=lambda x: x["speed"], reverse=True)
    return move_order


def battle_play_by_play(
    player_data: dict,
    enemies_to_fight: list[str],
    display_battle_params,
    player_choice: str,
    companion_choice: str = None,  # ? If None, companion is dead
    player_attack_target: str = None,  # ? If None, player isn't attacking
    item_choice: str = None,  # ? If None, player isn't using an item
    item_target_choice: str = None,  # ? If None, item target is implied or isn't using an item
):

    save_battle_data(create_enemies_battle_stats(player_data, enemies_to_fight))

    enemy_stats = reload_battle_data()
    player_data = reload_player_data()
    move_order = create_battle_move_order(player_data, enemy_stats)
    same_enemy_index = (
        0  # If 2 similar enemies, this keeps track of which is moving first
    )

    for index, move in enumerate(move_order):  # Loop through move_order
        if "player_name" in move.keys():  # If it's the player...
            if player_choice == "run away":
                return "ran away"
            if player_choice == "attack":
                if (
                    player_attack_target == "a" or player_attack_target == "b"
                ):  # If player attacks one of the two same named enemy
                    print(
                        color_text(
                            player_data["name"]
                            + " attacks "
                            + enemy_stats[0]["display_name"]
                            + " "
                            + player_attack_target.capitalize()
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )
                    press_space_to_continue()
                    add_vertical_spaces(1)
                else:  # If player attacks one enemy or a unique named enemy
                    print(
                        color_text(
                            player_data["name"]
                            + " attacks "
                            + player_attack_target
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )
                    press_space_to_continue()
                    add_vertical_spaces(1)
            if player_choice == "defend":
                print(
                    color_text(
                        player_data["name"] + " defends " + move_index_to_word(index),
                        player_data["color"],
                    )
                )
                press_space_to_continue()
                add_vertical_spaces(1)
            if player_choice == "use item":
                return "used item"

        if "companion_name" in move.keys():  # If it's the companion...
            if companion_choice == "attack":
                companion_attack_target = random_companion_attack_target(
                    player_data, enemy_stats
                )
                if companion_attack_target == "a" or companion_attack_target == "b":
                    print(
                        color_text(
                            player_data["companion_name"]
                            + " attacks "
                            + enemy_stats[0]["display_name"]
                            + " "
                            + companion_attack_target.capitalize()
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )
                    press_space_to_continue()
                    add_vertical_spaces(1)
                else:
                    print(
                        color_text(
                            player_data["companion_name"]
                            + " attacks "
                            + companion_attack_target
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )
                    press_space_to_continue()
                    add_vertical_spaces(1)
            if companion_choice == "defend":
                print(
                    color_text(
                        player_data["companion_name"]
                        + " defends "
                        + move_index_to_word(index),
                        player_data["color"],
                    )
                )
                press_space_to_continue()
                add_vertical_spaces(1)
            if companion_choice == "love you":
                print(
                    color_text(
                        player_data["companion_name"]
                        + " chooses to love "
                        + player_data["name"]
                        + " "
                        + move_index_to_word(index),
                        player_data["color"],
                    )
                )
                press_space_to_continue()
                add_vertical_spaces(1)
        if "sprite_name" in move.keys():  # If it's an enemy...
            enemy_choice = random_enemy_move()
            if enemy_choice == "attack":
                enemy_attack_target = random_enemy_attack_target(player_data)

                # If 2 similar enemies and one is attacking
                if len(enemy_stats) == 2 and enemy_stats[0] == enemy_stats[1]:
                    if same_enemy_index == 0:
                        print(
                            color_text(
                                move["display_name"]
                                + " A "
                                + "attacks "
                                + enemy_attack_target
                                + " "
                                + move_index_to_word(index),
                                "red",
                            )
                        )
                        same_enemy_index = 1
                        press_space_to_continue()
                        add_vertical_spaces(1)
                    else:
                        print(
                            color_text(
                                move["display_name"]
                                + " B "
                                + "attacks "
                                + enemy_attack_target
                                + " "
                                + move_index_to_word(index),
                                "red",
                            )
                        )
                        press_space_to_continue()
                        add_vertical_spaces(1)
                else:
                    print(
                        color_text(
                            move["display_name"]
                            + " attacks "
                            + enemy_attack_target
                            + " "
                            + move_index_to_word(index),
                            "red",
                        )
                    )
                    press_space_to_continue()
                    add_vertical_spaces(1)
            if enemy_choice == "defend":
                print(
                    color_text(
                        move["display_name"] + " defends " + move_index_to_word(index),
                        "red",
                    )
                )
                press_space_to_continue()
                add_vertical_spaces(1)

    ask_battle_questions(enemies_to_fight, player_data, display_battle_params)
