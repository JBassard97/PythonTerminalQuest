from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from assets.large_ascii_sprites import print_single_large_sprite
from assets.battle_ascii_sprites import print_battle_sprites_side_by_side
from lore.dialogue_dict import dialogue_dict


def print_multiple_dialogues(
    dialogue_portion: dict, start_line: int, end_line_plus_one: int
):
    for i in range(start_line, end_line_plus_one):
        print(dialogue_portion[i])
        add_vertical_spaces(1)


def print_large_sprite_with_buffer(sprite_name: str, sprite_color: str = None):
    if sprite_color is None:
        add_vertical_spaces(1)
        print_single_large_sprite(sprite_name)
        add_vertical_spaces(1)
    else:
        add_vertical_spaces(1)
        print_single_large_sprite(sprite_name, sprite_color)
        add_vertical_spaces(1)


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


# Player_data will be run through this function to add fields after completing intro_story
# "completed_stories" will be used to measure story progression
def add_starting_stats(player_data: dict):
    #! These apply to all weapon_classes
    player_data["completed_stories"] = ["intro_story"]
    player_data["item_inventory"] = []
    player_data["battles_completed"] = 0
    player_data["current_funds"] = 100
    player_data["diamond_shards_obtained"] = 0

    player_data["player_max_health"] = 100
    player_data["player_current_health"] = 100
    player_data["player_max_attack"] = 500
    player_data["player_max_defense"] = 500
    player_data["player_max_speed"] = 500

    player_data["companion_max_health"] = 50
    player_data["companion_max_attack"] = 300
    player_data["companion_max_defense"] = 300
    player_data["companion_max_speed"] = 300
    player_data["companion_current_health"] = 50
    player_data["companion_current_attack"] = 50
    player_data["companion_current_defense"] = 50
    player_data["companion_current_speed"] = 50
    player_data["is_companion_alive"] = True

    #! "attack_boost" is a multiplier, NOT an addition
    weapon_class = player_data["weapon_class"]
    if weapon_class == "archer":  #! If Archer...
        player_data["current_weapon"] = {
            "name": "Basic Hunter Bow",
            "attack_boost": 1,
        }
        player_data["current_attack"] = 50  # LOW
        player_data["current_defense"] = 100  # MID
        player_data["current_speed"] = 150  # HIGH
    if weapon_class == "swordsman":  #! If Swordsman
        player_data["current_weapon"] = {
            "name": "Inherited Blunt Sword",
            "attack_boost": 1,
        }
        player_data["current_attack"] = 100  # MID
        player_data["current_defense"] = 150  # HIGH (because they have a shield)
        player_data["current_speed"] = 50  # LOW
    if weapon_class == "magician":  #! If Magician...
        player_data["current_weapon"] = {
            "name": "Lushgrove Tree Branch",
            "attack_boost": 1,
        }
        player_data["current_attack"] = 150  # HIGH
        player_data["current_defense"] = 50  # LOW
        player_data["current_speed"] = 100  # SPEED

    player_data["current_realm"] = "tutorial"
    return player_data
