from db.db_functions import (
    reload_player_data,
    reload_battle_data,
    save_player_data,
    save_battle_data,
)
from utils.battles.battle_helpers import find_enemy_index_by_display_name
import math

#! ATTACK


def player_perform_attack(
    player_attack_target: str, is_enemy_a_defending: bool, is_enemy_b_defending: bool
):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()

    if len(enemy_stats) == 2:
        if enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]:
            if player_attack_target == "a":
                enemy_index = 0
            elif player_attack_target == "b":
                enemy_index = 1
        else:
            enemy_index = find_enemy_index_by_display_name(player_attack_target)
    else:
        enemy_index = 0

    weapon_damage = player_data["current_weapon"]["base_damage"]
    player_attack = player_data["current_attack"] / 100
    raw_damage = weapon_damage + (weapon_damage * player_attack)

    enemy_defense: int = enemy_stats[enemy_index]["defense"] / 100
    if (enemy_index == 0 and is_enemy_a_defending) or (
        enemy_index == 1 and is_enemy_b_defending
    ):
        defense_bonus = 0.30
        enemy_defense += defense_bonus

    true_damage = math.ceil(raw_damage - (raw_damage * enemy_defense))
    print(true_damage)


def companion_perform_attack(
    companion_attack_target: str, is_enemy_a_defending: bool, is_enemy_b_defending: bool
):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()
    pass


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
