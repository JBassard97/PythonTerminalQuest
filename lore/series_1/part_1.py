# INTRO STORY DIALOGUE

from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from assets.battle_ascii_sprites import print_battle_sprites_side_by_side
from lore.dialogue_dict import dialogue_dict
from lore.dialogue_helpers import (
    print_large_sprite_with_buffer,
    print_multiple_dialogues,
)


def dialogue_series_1_part_1(player_data: dict):
    dialogue_portion = dialogue_dict["series_1"]["part_1"]

    reset_screen()
    print(dialogue_portion[1])
    add_vertical_spaces(1)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print(dialogue_portion[2])
    print_large_sprite_with_buffer("world_map")
    print_multiple_dialogues(dialogue_portion, 3, 7)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print(dialogue_portion[7])
    print_large_sprite_with_buffer("pythonia_castle", "blue")
    press_space_to_continue()
    # --------------------
    reset_screen()
    print(dialogue_portion[8])
    print_large_sprite_with_buffer("diamond_of_destiny")
    print(dialogue_portion[9])
    add_vertical_spaces(1)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print_multiple_dialogues(dialogue_portion, 10, 13)
    print_large_sprite_with_buffer("null_realm", "magenta")
    print_multiple_dialogues(dialogue_portion, 13, 17)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print_multiple_dialogues(dialogue_portion, 17, 20)
    print_large_sprite_with_buffer("daemon_the_shadow_process", "red")
    print_multiple_dialogues(dialogue_portion, 20, 22)
    press_space_to_continue()
    # --------------------
    reset_screen()
    add_vertical_spaces(2)
    print_multiple_dialogues(dialogue_portion, 22, 24)
    press_space_to_continue()
    # --------------------
    reset_screen()
    add_vertical_spaces(2)
    print(dialogue_portion[24])
    add_vertical_spaces(3)
    print_multiple_dialogues(dialogue_portion, 25, 27)
    press_space_to_continue()
    # --------------------
    reset_screen()
    add_vertical_spaces(2)
    print(dialogue_portion[27])
    add_vertical_spaces(3)
    print_multiple_dialogues(dialogue_portion, 28, 31)
    press_space_to_continue()
    # --------------------
    reset_screen()
    add_vertical_spaces(2)
    player_color = player_data["color"]
    print(
        color_text("The next morning, a young ", "cyan")
        + color_text(
            f'{player_data["weapon_class"]} ',
            player_color,
        )
        + color_text("named ", "cyan")
        + color_text(f'{player_data["name"]} ', player_color)
        + color_text(
            "awoke to a horseman shouting the new decrees throughout Pythonia's castle town streets.",
            "cyan",
        )
    )
    add_vertical_spaces(3)
    print(
        color_text(
            f'"Wakey wakey {player_data["companion_name"]}, it sounds like we have a quest we cannot afford to sleep through this time."',
            player_color,
        )
    )
    add_vertical_spaces(1)
    print(
        color_text(
            f'The {player_data["companion_type"]} groggily rose out of bed and nodded its head in reluctant agreement.',
            "cyan",
        )
    )
    add_vertical_spaces(1)
    print_battle_sprites_side_by_side(
        [player_data["weapon_class"], player_data["companion_type"]], player_color
    )
    add_vertical_spaces(1)
    print(dialogue_portion[31])
    add_vertical_spaces(3)
    press_space_to_continue()
    reset_screen()


# Player_data will be run through this function to add fields after completing intro_story
# "completed_stories" will be used to measure story progression
def add_starting_stats(player_data: dict):
    #! These apply to all weapon_classes
    player_data["completed_stories"] = ["intro_story"]
    player_data["item_inventory"] = ["potion", "potion", "throwing knife"]
    player_data["stored_weapons"] = []
    player_data["item_inventory_capacity"] = 10
    player_data["total_battles_completed"] = 0
    player_data["battles_completed_in_realm"] = 0
    player_data["current_funds"] = 100
    player_data["diamond_shards_obtained"] = 0

    player_data["player_max_health"] = 100
    player_data["player_current_health"] = 100
    player_data["player_max_attack"] = 100
    player_data["player_max_defense"] = 100
    player_data["player_max_speed"] = 100
    player_data["player_critical_percent"] = 5

    player_data["companion_max_health"] = 50
    player_data["companion_max_attack"] = 100
    player_data["companion_max_defense"] = 100
    player_data["companion_max_speed"] = 100
    player_data["companion_critical_percent"] = 5

    player_data["companion_current_health"] = 50
    player_data["companion_current_attack"] = 10
    player_data["companion_current_defense"] = 20
    player_data["companion_current_speed"] = 20
    player_data["is_companion_alive"] = True

    weapon_class = player_data["weapon_class"]
    if weapon_class == "archer":  #! If Archer...
        player_data["current_weapon"] = {
            "name": "Basic Hunter Bow",
            "description": "A bow fit for feeding your family with wild squirrels",
            "base_damage": 10,
            "resell_price": 5,
        }
        player_data["current_attack"] = 20  # LOW
        player_data["current_defense"] = 35  # MID
        player_data["current_speed"] = 50  # HIGH
    if weapon_class == "swordsman":  #! If Swordsman
        player_data["current_weapon"] = {
            "name": "Inherited Blunt Sword",
            "description": "A sword passed down in your family, has seen some battles",
            "base_damage": 10,
            "resell_price": 5,
        }
        player_data["current_attack"] = 35  # MID
        player_data["current_defense"] = 50  # HIGH (because they have a shield)
        player_data["current_speed"] = 20  # LOW (because the shield is heavy)
    if weapon_class == "magician":  #! If Magician...
        player_data["current_weapon"] = {
            "name": "Lushgrove Tree Branch",
            "description": "An ordinary branch that has been blessed for minor magic casting",
            "base_damage": 10,
            "resell_price": 5,
        }
        player_data["current_attack"] = 50  # HIGH
        player_data["current_defense"] = 20  # LOW
        player_data["current_speed"] = 35  # SPEED

    # ! Stored stats used to handle resetting buffs at battle end
    player_data["player_stored_attack"] = player_data["current_attack"]
    player_data["player_stored_defense"] = player_data["current_defense"]
    player_data["player_stored_speed"] = player_data["current_speed"]

    player_data["companion_stored_attack"] = player_data["companion_current_attack"]
    player_data["companion_stored_defense"] = player_data["companion_current_defense"]
    player_data["companion_stored_speed"] = player_data["companion_current_speed"]

    player_data["current_realm"] = "tutorial"
    return player_data
