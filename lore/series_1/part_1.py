from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from assets.large_ascii_sprites import print_single_large_sprite
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
