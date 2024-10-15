# MEETING WISE WITCH DIALOGUE

from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from lore.dialogue_dict import dialogue_dict
from lore.dialogue_helpers import (
    print_large_sprite_with_buffer,
    print_multiple_dialogues,
)


def dialogue_series_1_part_2(player_data: dict):
    dialogue_portion = dialogue_dict["series_1"]["part_2"]
