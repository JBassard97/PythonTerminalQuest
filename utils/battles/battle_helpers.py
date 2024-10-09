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
    clear_battle_db,
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
    if len(enemy_stats) == 2 and enemy_stats[0] == enemy_stats[1]:
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
def display_battle():
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()

    protags_to_fight: list[str] = [player_data["weapon_class"]]
    if player_data["is_companion_alive"]:
        protags_to_fight.append(player_data["companion_type"])
    protag_string: str = create_protag_string(protags_to_fight, player_data)

    enemies_to_fight: list[str] = []
    for enemy in enemy_stats:
        enemies_to_fight.append(enemy["sprite_name"])
    enemy_string: str = create_enemy_string(enemies_to_fight, player_data)

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

    if len(enemy_stats) == 2:
        if enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]:
            print(color_text(enemy_stats[0]["display_name"] + " A's stats:", "red"))
            print(f'Health: {enemy_stats[0]["health"]}/{enemy_stats[0]["max_health"]}')
            add_vertical_spaces(1)
            print(color_text(enemy_stats[1]["display_name"] + " B's stats:", "red"))
            print(f'Health: {enemy_stats[1]["health"]}/{enemy_stats[1]["max_health"]}')
            add_vertical_spaces(1)
        else:
            for enemy in enemy_stats:
                print(color_text(enemy["display_name"] + "'s stats:", "red"))
                print(f'Health: {enemy["health"]}/{enemy["max_health"]}')
                add_vertical_spaces(1)
    else:
        print(color_text(enemy_stats[0]["display_name"] + "'s stats:", "red"))
        print(f'Health: {enemy_stats[0]["health"]}/{enemy_stats[0]["max_health"]}')
        add_vertical_spaces(1)


def create_enemies_battle_stats(enemies_to_fight: list[str]):
    player_data = reload_player_data()

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


# Returns the index of a dict in a list given a key and property value to search
def find_enemy_index_by_display_name(value: str):
    enemy_stats: list[dict] = reload_battle_data()
    return next(
        (
            index
            for index, d in enumerate(enemy_stats)
            if d.get("display_name") == value
        ),
        -1,
    )
