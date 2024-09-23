from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from assets.large_ascii_sprites import print_single_large_sprite
from lore.dialogue_dict import dialogue_dict


def dialogue_series_1_part_1(player_data: dict):
    dialogue_portion = dialogue_dict["series_1"]["part_1"]

    reset_screen()
    print(dialogue_portion[1])
    add_vertical_spaces(1)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print(dialogue_portion[2])
    add_vertical_spaces(1)
    print_single_large_sprite("world_map")
    add_vertical_spaces(1)
    for i in range(3, 7):
        print(dialogue_portion[i])
        add_vertical_spaces(1)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print(dialogue_portion[7])
    add_vertical_spaces(1)
    print_single_large_sprite("pythonia_castle", "blue")
    add_vertical_spaces(1)
    press_space_to_continue()
    # --------------------
    reset_screen()
    print(dialogue_portion[8])
    add_vertical_spaces(1)
    print_single_large_sprite("diamond_of_destiny")
    add_vertical_spaces(1)
    print(dialogue_portion[9])
    add_vertical_spaces(1)
    press_space_to_continue()
    # ---------------------
    reset_screen()
    for i in range(10, 13):
        print(dialogue_portion[i])
        add_vertical_spaces(1)
    print_single_large_sprite("null_realm", "red")
    add_vertical_spaces(1)
    for i in range(13, 17):
        print(dialogue_portion[i])
        add_vertical_spaces(1)
    press_space_to_continue()
    # --------------------
