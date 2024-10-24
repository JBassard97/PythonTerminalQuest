from db.db_functions import (
    reload_player_data,
    reload_battle_data,
    save_player_data,
    save_battle_data,
    clear_battle_db,
)
from db.item_db import item_data
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
    print_item_target_healed,
    print_health_maxed_out,
    print_random_love_heal_action,
    print_random_love_buff_action,
    print_target_buffed,
)
import random
import math
from utils.helpers import color_text, percent_chance_true


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

    #! Critical Hit
    if percent_chance_true(player_data["player_critical_percent"]):
        true_damage = true_damage + (true_damage * 0.50)
        print("Critical Hit!")

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

    #! Critical Hit
    if percent_chance_true(player_data["companion_critical_percent"]):
        true_damage = true_damage + (true_damage * 0.50)
        print("Critical Hit!")


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

    if percent_chance_true(10): #! Critical Hit
        true_damage = true_damage + (true_damage * 0.50)
        print("Critical Hit!")


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


def player_perform_use_item(item_choice: str, item_target_choice: str):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()

    # ! If it's a heal item...
    if item_choice in item_data["heal_items"]:
        heal_value: int = item_data["heal_items"][item_choice]["heal_value"]
        print_item_target_healed(heal_value, item_target_choice)

        if item_target_choice == player_data["name"]:
            player_data["player_current_health"] += heal_value
            if player_data["player_current_health"] > player_data["player_max_health"]:
                print_health_maxed_out(item_target_choice)
                player_data["player_current_health"] = player_data["player_max_health"]

        elif item_target_choice == player_data["companion_name"]:
            player_data["companion_current_health"] += heal_value
            if (
                player_data["companion_current_health"]
                > player_data["companion_max_health"]
            ):
                print_health_maxed_out(item_target_choice)
                player_data["companion_current_health"] = player_data[
                    "companion_max_health"
                ]

        player_data["item_inventory"].remove(item_choice)
        save_player_data(player_data)

    # ! If it's a buff item...
    if item_choice in item_data["buff_items"]:
        if "attack_boost" in item_data["buff_items"][item_choice]:
            stat_boosted = "attack"
            boost = item_data["buff_items"][item_choice]["attack_boost"]
        elif "defense_boost" in item_data["buff_items"][item_choice]:
            stat_boosted = "defense"
            boost = item_data["buff_items"][item_choice]["defense_boost"]
        elif "speed_boost" in item_data["buff_items"][item_choice]:
            stat_boosted = "speed"
            boost = item_data["buff_items"][item_choice]["speed_boost"]

        if item_target_choice == player_data["name"]:
            stat_target = "current_" + stat_boosted
            max_target = "player_max_" + stat_boosted
        elif item_target_choice == player_data["companion_name"]:
            stat_target = "companion_current_" + stat_boosted
            max_target = "companion_max_" + stat_boosted

        print_target_buffed(boost, stat_boosted, item_target_choice)

        player_data[stat_target] = player_data[stat_target] + math.ceil(
            player_data[stat_target] * (boost / 100)
        )

        # ? Preventing stat boosts from going beyond maximums
        if player_data[stat_target] > player_data[max_target]:
            player_data[stat_target] = player_data[max_target]

        player_data["item_inventory"].remove(item_choice)
        save_player_data(player_data)

    # ! If it's a battle item
    # Battle Items ignore enemy defense and perform flat rate damages
    if item_choice in item_data["battle_items"]:
        damage_value = item_data["battle_items"][item_choice]["damage_value"]
        enemy_index = return_enemy_index(enemy_stats, item_target_choice)

        print_true_damage_to_enemy(enemy_stats, item_target_choice, damage_value)
        enemy_stats[enemy_index]["health"] -= damage_value
        if enemy_stats[enemy_index]["health"] > 0:
            save_battle_data(enemy_stats)
        else:  # ! If your attack kills...
            print_enemy_has_been_slain(enemy_stats, item_target_choice)
            del enemy_stats[enemy_index]
            if len(enemy_stats) == 0:
                clear_battle_db()
                return "win"
            else:
                save_battle_data(enemy_stats)

        player_data["item_inventory"].remove(item_choice)
        save_player_data(player_data)

    return None


#! LOVE


def companion_perform_love():
    player_data = reload_player_data()
    specific_love = random.choice(["heal player", "find item", "buff player"])

    if specific_love == "heal player":
        health_deficit = (
            player_data["player_max_health"] - player_data["player_current_health"]
        )

        print_random_love_heal_action()

        if health_deficit == 0:
            print(color_text("But your health was already full!", "green"))
        else:
            random_recovery = random.randint(1, health_deficit)
            print(
                color_text(f"And helped you recover {random_recovery} health!", "green")
            )
            player_data["player_current_health"] += random_recovery
            save_player_data(player_data)

    elif specific_love == "find item":
        findable_items = []
        heal_items = list(item_data["heal_items"])
        buff_items = list(item_data["buff_items"])
        battle_items = list(item_data["battle_items"])
        findable_items += heal_items + buff_items + battle_items
        random_item = random.choice(findable_items)

        sniffers = ["dog", "wolf", "bear"]
        flyers = ["falcon", "crow", "flamingo", "owl"]
        if player_data["companion_type"] in sniffers:
            verb = "sniffed"
        elif player_data["companion_type"] in flyers:
            verb = "flew"
        else:
            verb = "scavenged"

        print(
            color_text(
                "Your companion "
                + verb
                + " around the area and found a "
                + random_item
                + "!",
                "cyan",
            )
        )

        player_data["item_inventory"].append(random_item)
        save_player_data(player_data)

    if specific_love == "buff player":
        random_stat = random.choice(["attack", "defense", "speed"])
        stat_target = "current_" + random_stat
        boost = 20

        print_random_love_buff_action(random_stat)
        print_target_buffed(boost, random_stat, player_data["name"])

        player_data[stat_target] = player_data[stat_target] + math.ceil(
            player_data[stat_target]
            * ((boost / 100) * (player_data["diamond_shards_obtained"] + 1))
        )
        save_player_data(player_data)

    # FOR NOW
    return None
