from db.db_functions import (
    reload_player_data,
    reload_battle_data,
    save_player_data,
    save_battle_data,
    clear_battle_db,
)
from utils.battles.battle_helpers import (
    return_enemy_index,
    find_enemy_index_by_display_name,
    calculate_raw_player_damage,
    calculate_enemy_defense,
    calculate_true_damage,
    print_true_damage_to_enemy,
    print_enemy_has_been_slain,
    calculate_player_or_companion_defense,
    print_true_damage_to_player_or_companion,
    print_companion_has_been_slain,
)
from utils.helpers import color_text
import math

#! ATTACK


def player_perform_attack(
    player_attack_target: str, is_enemy_a_defending: bool, is_enemy_b_defending: bool
):
    player_data = reload_player_data()
    raw_damage = calculate_raw_player_damage(player_data)

    enemy_stats = reload_battle_data()
    enemy_index = return_enemy_index(enemy_stats, player_attack_target)
    enemy_defense = calculate_enemy_defense(
        enemy_stats, enemy_index, is_enemy_a_defending, is_enemy_b_defending
    )
    true_damage = calculate_true_damage(raw_damage, enemy_defense)

    print_true_damage_to_enemy(enemy_stats, player_attack_target, true_damage)

    enemy_stats[enemy_index]["health"] -= true_damage
    if enemy_stats[enemy_index]["health"] > 0:
        save_battle_data(enemy_stats)
    else:  # ! If your attack kills...
        print_enemy_has_been_slain(enemy_stats, player_attack_target)
        del enemy_stats[enemy_index]
        if len(enemy_stats) == 0:
            clear_battle_db()
            return "win"
        else:
            save_battle_data(enemy_stats)


def companion_perform_attack(
    companion_attack_target: str, is_enemy_a_defending: bool, is_enemy_b_defending: bool
):
    player_data = reload_player_data()
    raw_damage = player_data["companion_current_attack"]

    enemy_stats = reload_battle_data()
    enemy_index = return_enemy_index(enemy_stats, companion_attack_target)
    enemy_defense = calculate_enemy_defense(
        enemy_stats, enemy_index, is_enemy_a_defending, is_enemy_b_defending
    )
    true_damage = calculate_true_damage(raw_damage, enemy_defense)

    print_true_damage_to_enemy(enemy_stats, companion_attack_target, true_damage)
    enemy_stats[enemy_index]["health"] -= true_damage
    if enemy_stats[enemy_index]["health"] > 0:
        save_battle_data(enemy_stats)
    else:  # ! If companion's attack kills...
        print_enemy_has_been_slain(enemy_stats, companion_attack_target)
        del enemy_stats[enemy_index]
        if len(enemy_stats) == 0:
            clear_battle_db()
            return "win"
        else:
            save_battle_data(enemy_stats)


def enemy_perform_attack(
    enemy_display_name: str,
    enemy_attack_target: str,
    is_player_defending: bool,
    is_companion_defending: bool,
):
    enemy_stats = reload_battle_data()
    if (
        len(enemy_stats) == 2
        and enemy_stats[0]["display_name"] != enemy_stats[1]["display_name"]
    ):
        enemy_index = find_enemy_index_by_display_name(enemy_display_name)
        raw_damage = enemy_stats[enemy_index]["attack"]
    else:
        raw_damage = enemy_stats[0]["attack"]

    player_data = reload_player_data()
    target_defense = calculate_player_or_companion_defense(
        player_data, enemy_attack_target, is_player_defending, is_companion_defending
    )
    true_damage = calculate_true_damage(raw_damage, target_defense)

    print_true_damage_to_player_or_companion(enemy_attack_target, true_damage)

    if enemy_attack_target == player_data["name"]:
        player_data["player_current_health"] -= true_damage
        if player_data["player_current_health"] > 0:
            save_player_data(player_data)
        else:
            player_data["player_current_health"] = 0
            save_player_data(player_data)
            return "lose"

    if enemy_attack_target == player_data["companion_name"]:
        player_data["companion_current_health"] -= true_damage
        if player_data["companion_current_health"] > 0:
            save_player_data(player_data)
        else:
            print_companion_has_been_slain(enemy_attack_target)
            player_data["companion_current_health"] = 0
            player_data["is_companion_alive"] = False
            save_player_data(player_data)


#! USE ITEM


def player_perform_use_item():
    pass


#! LOVE


def companion_perform_love():
    pass
