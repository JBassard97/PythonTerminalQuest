from utils.helpers import add_vertical_spaces
from assets.large_ascii_sprites import print_single_large_sprite


def print_large_sprite_with_buffer(sprite_name: str, sprite_color: str = None):
    if sprite_color is None:
        add_vertical_spaces(1)
        print_single_large_sprite(sprite_name)
        add_vertical_spaces(1)
    else:
        add_vertical_spaces(1)
        print_single_large_sprite(sprite_name, sprite_color)
        add_vertical_spaces(1)


def print_multiple_dialogues(
    dialogue_portion: dict, start_line: int, end_line_plus_one: int
):
    for i in range(start_line, end_line_plus_one):
        print(dialogue_portion[i])
        add_vertical_spaces(1)
