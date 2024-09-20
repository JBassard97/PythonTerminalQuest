from utils.helpers import color_text

sprite_dict = {  # each sprite is 12 x 22
    "archer": {
        "a": r"                      ",
        "b": r"        .    ____     ",
        "c": r"      .' \  / \==\    ",
        "d": r"     /    \ - o\ |    ",
        "e": r"    /_.----\\__,-----.",
        "f": r"<--(\_|_____<__|_____/",
        "g": r"    \  ````/|   ``/```",
        "h": r"     `.   / |    I|   ",
        "i": r"       `./  |____I|   ",
        "j": r"            \ \ I |   ",
        "k": r"           _|_|_I_|   ",
        "l": r"          /__/____|   ",
    },
    "falcon": {
        "a": r"                   ",
        "b": r"                   ",
        "c": r"         __        ",
        "d": r"        /-{>       ",
        "e": r"    ____) (____    ",
        "f": r"  //'--;   ;--'\\  ",
        "g": r" ///////\_/\\\\\\\ ",
        "h": r"      / m m \      ",
        "i": r"     /VVVVVVV\     ",
        "j": r"    | | | | | |    ",
        "k": r"                   ",
        "l": r"                   ",
    },
    "wolf": {
        "a": r"                      ",
        "b": r"  .                   ",
        "c": r"/V \.                 ",
        "d": r"\  ` \.               ",
        "e": r" |   >>               ",
        "f": r" |    \.              ",
        "g": r" |      \.            ",
        "h": r" |        \.          ",
        "i": r"  \ /  /    \.        ",
        "j": r"  | | (      )        ",
        "k": r"  | |  _\_   |______  ",
        "l": r" (__/(_______/_______>",
    },
    "spider": {
        "a": r'   /\  .-"""-.  /\   ',
        "b": r"  //\\/  ,,,  \//\\  ",
        "c": r"   /\| ,;;;;;, |/\|  ",
        "d": r'  //\\\;-"""-;///\\  ',
        "e": r" //  \/   .   \/  \\ ",
        "f": r"(| ,-_| \ | / |_-, |)",
        "g": r"  //`__\.-.-./__`\\  ",
        "h": r" // /.-(() ())-.\ \\ ",
        "i": r"(\ |)   '---'   (| /)",
        "j": r" ` (|           |) ` ",
        "k": r"   \)           (/   ",
        "l": r"                     ",
    },
    "bear": {
        "a": r"     (()__(()        ",
        "b": r"     /       \       ",
        "c": r"    (  0  0   \.     ",
        "d": r"     \(_()_)  /      ",
        "e": r"     /         \     ",
        "f": r"    / _ ---____ \.   ",
        "g": r"   (     |       )   ",
        "h": r"   /\_.----'-.__/\_  ",
        "i": r"  / (        /     \ ",
        "j": r"  \  \      (      / ",
        "k": r"   )  '._____)    /  ",
        "l": r"(((____.--(((____/   ",
    },
    "cat": {
        "a": r"                     ",
        "b": r"                     ",
        "c": r"                     ",
        "d": r"                     ",
        "e": r"                     ",
        "f": r"              _ |\_  ",
        "g": r"              \` ..\ ",
        "h": r'         __,.-" =__Y=',
        "i": r'       ."        )   ',
        "j": r" _    /   ,    \/\_  ",
        "k": r"((____|    )_-\ \_-` ",
        "l": r"`-----'`-----` `--`  ",
    },
    "magician": {
        "a": r"          . _\/_  . ",
        "b": r"           . \\  .  ",
        "c": r"       .==. ` \\'   ",
        "d": r".\|   //--\\   \,   ",
        "e": r"\_'`._\\__//_.'`.;  ",
        "f": r"  `.__      __,' \\ ",
        "g": r"      ||  ||      \\",
        "h": r"      ||  ||       `",
        "i": r"      ||  ||        ",
        "j": r"      ||  ||        ",
        "k": r"      ||__||        ",
        "l": r"     =='  '==       ",
    },
    "swordsman": {
        "a": r".^.                ",
        "b": r"|||                ",
        "c": r"|||       _T_      ",
        "d": r"|||   .-.[:|:].-.  ",
        "e": r'===_ /\|  """  |   ',
        "f": r" E]_|\/ \--|-|''''|",
        "g": r" O  `'  '=[:]|    |",
        "h": r'         """"|    |',
        "i": r"        '[][]'.__.'",
        "j": r'      /[]/"""\[]\  ',
        "k": r"      | |     | |  ",
        "l": r"    <\\\)     (///>",
    },
    "x": {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
    },
    "x": {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
    },
    "x": {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
    },
    "x": {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
    },
    "x": {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
    },
}


def sprite_test_print():
    print("\n\nBEGIN SPRITE TEST PRINT\n")

    for sprite in sprite_dict:
        print(f"{sprite}")
        for line in sprite_dict[sprite].values():
            print(line)
        else:
            print("")


def print_sprites_side_by_side(
    enemy_sprites: list,
    enemy_color: str,
    protag_sprites: list = None,
    protag_color: str = None,
):
    # Create dictionaries for enemy sprites
    enemy_lines = {key: sprite_dict[key] for key in enemy_sprites}

    # Optional: Initialize protagonist lines only if protag_sprites is provided
    protag_lines = (
        {key: sprite_dict[key] for key in protag_sprites} if protag_sprites else {}
    )

    spacing = "          "

    # Iterate over each line (a to l)
    for line_key in "abcdefghijkl":
        # Combine enemy sprite lines
        combined_line = "  ".join(
            color_text(enemy_lines[sprite_name][line_key], enemy_color)
            for sprite_name in enemy_sprites
        )

        # Add protagonist sprite lines if they exist
        if protag_sprites:
            combined_line += spacing + "  ".join(
                color_text(protag_lines[sprite_name][line_key], protag_color)
                for sprite_name in protag_sprites
            )

        print(combined_line)


# def print_sprites_side_by_side(
#     enemy_sprites: list,
#     enemy_color: str,
#     protag_sprites: list = None,
#     protag_color: str = None,
# ):
#     # Create dictionaries for enemy and protagonist sprites
#     enemy_lines = {key: sprite_dict[key] for key in enemy_sprites}
#     protag_lines = {key: sprite_dict[key] for key in protag_sprites}

#     spacing = "          "

#     # Iterate over each line (a to l)
#     for line_key in "abcdefghijkl":
#         # Combine enemy and protagonist sprite lines side by side
#         combined_line = (
#             "  ".join(
#                 color_text(enemy_lines[sprite_name][line_key], enemy_color)
#                 for sprite_name in enemy_sprites
#             )
#             + spacing
#             + "  ".join(
#                 color_text(protag_lines[sprite_name][line_key], protag_color)
#                 for sprite_name in protag_sprites
#             )
#         )

#         print(combined_line)
