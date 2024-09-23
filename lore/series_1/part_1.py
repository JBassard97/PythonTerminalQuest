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
    for i in range(1, 6):
        print(dialogue_portion[i])
        add_vertical_spaces(1)

    press_space_to_continue()
    reset_screen()

    # print(dialogue_portion[6])
    add_vertical_spaces(2)
    print_single_large_sprite("pythonia_castle", "blue")
    add_vertical_spaces(1)
    press_space_to_continue()
