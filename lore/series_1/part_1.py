from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from lore.dialogue_dict import dialogue_dict


def dialogue_series_1_part_1(player_data: dict):
    dialogue_portion = dialogue_dict["series_1"]["part_1"]

    reset_screen()
    print(dialogue_portion[1])
    press_space_to_continue()
