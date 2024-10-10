from db.db_functions import (
    reload_player_data,
    reload_battle_data,
    save_player_data,
    save_battle_data,
)
from utils.battles.battle_helpers import (
    return_enemy_index,
    calculate_raw_player_damage,
    calculate_enemy_defense,
    calculate_true_damage_to_enemy,
    print_true_damage_to_enemy,
    print_enemy_has_been_slain,
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
    true_damage = calculate_true_damage_to_enemy(raw_damage, enemy_defense)

    print_true_damage_to_enemy(enemy_stats, player_attack_target, true_damage)

    enemy_stats[enemy_index]["health"] -= true_damage
    if enemy_stats[enemy_index]["health"] > 0:
        save_battle_data(enemy_stats)
    else:  # ! If your attack kills...
        del enemy_stats[enemy_index]
        print_enemy_has_been_slain(enemy_stats, player_attack_target)
        if len(enemy_stats) == 0:
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
    true_damage = calculate_true_damage_to_enemy(raw_damage, enemy_defense)

    print_true_damage_to_enemy(enemy_stats, companion_attack_target, true_damage)
    enemy_stats[enemy_index]["health"] -= true_damage
    if enemy_stats[enemy_index]["health"] > 0:
        save_battle_data(enemy_stats)
    else:  # ! If companion's attack kills...
        del enemy_stats[enemy_index]
        print_enemy_has_been_slain(enemy_stats, companion_attack_target)
        if len(enemy_stats) == 0:
            return "win"
        else:
            save_battle_data(enemy_stats)


def unique_enemy_perform_attack(
    enemy_attack_target: str, is_player_defending: bool, is_companion_defending: bool
):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()
    pass


def similar_enemy_perfrom_attack(
    enemy_attack_target: str, is_player_defending: bool, is_companion_defending: bool
):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()
    pass


#! DEFEND


def player_perform_defend():
    pass


def companion_perform_defend():
    pass


def unique_enemy_perform_attack():
    pass


def enemy_a_perform_attack():
    pass


def enemy_b_perform_attack():
    pass


#! USE ITEM


def player_perform_use_item():
    pass


#! LOVE


def companion_perform_love():
    pass
