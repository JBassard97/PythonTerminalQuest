from utils.helpers import color_text

battle_sprite_dict = {  # each sprite is within 12 x 22
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
    "owl": {
        "a": r"                ",
        "b": r"                ",
        "c": r"  __________    ",
        "d": r" / ___  ___ \.  ",
        "e": r"/ / @ \/ @ \ \. ",
        "f": r"\ \___/\___/ /\.",
        "g": r" \____\/____/|| ",
        "h": r" /     /\\\\\// ",
        "i": r"|     |\\\\\\   ",
        "j": r" \      \\\\\\  ",
        "k": r"   \______/\\\\ ",
        "l": r"    _||_||_     ",
    },
    "scorpion": {
        "a": r"   ___    ___    ",
        "b": r"  ( _<    >_ )   ",
        "c": r"  //        \\   ",
        "d": r"  \\___..___//   ",
        "e": r"   `-(    )-'    ",
        "f": r"     _|__|_      ",
        "g": r"   ./_|__|_\.    ",
        "h": r"   ./_|__|_\.    ",
        "i": r"     \ || /  _)  ",
        "j": r"       ||   ( )  ",
        "k": r"       \\___//   ",
        "l": r"        `---'    ",
    },
    "dog": {
        "a": r"                      ",
        "b": r"                      ",
        "c": r"                      ",
        "d": r"                      ",
        "e": r"                      ",
        "f": r"                      ",
        "g": r"    ___               ",
        "h": r' __/_  `.  .-"""-.    ',
        "i": r" \_,` | \-'  /   )`-')",
        "j": r'  "") `"`    \  ((`"` ',
        "k": r" ___Y  ,    .'7 /|    ",
        "l": r"(_,___/...-` (_/_/    ",
    },
    "crow": {
        "a": r"                     ",
        "b": r"                     ",
        "c": r"                     ",
        "d": r"                     ",
        "e": r"                     ",
        "f": r"                     ",
        "g": r"    .--.             ",
        "h": r" _,-o   \.           ",
        "i": r"~ --.  , `--__       ",
        "j": r"      \`-_____~-___  ",
        "k": r"       `/~\--~~~~~--'",
        "l": r"       ^   ^         ",
    },
    "flamingo": {
        "a": r"               ",
        "b": r"               ",
        "c": r"     _         ",
        "d": r"----(O)        ",
        "e": r"      \.       ",
        "f": r"       \_      ",
        "g": r"       ( `'--.,",
        "h": r"        `,___/ ",
        "i": r"          |_\. ",
        "j": r"         /|    ",
        "k": r"         `|    ",
        "l": r"          ^    ",
    },
    "frog": {
        "a": r"                    ",
        "b": r"                    ",
        "c": r"                    ",
        "d": r"                    ",
        "e": r"                    ",
        "f": r"        _   _       ",
        "g": r"       (.)_(.)      ",
        "h": r"    _ (   _   ) _   ",
        "i": r"  ./ \/`-----'\/ \. ",
        "j": r" __\ ( (     ) ) /__",
        "k": r" )   /\ \._./ /\   (",
        "l": r"  )_/ /|\   /|\ \_( ",
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


def battle_sprite_test_print():
    print("\n\nBEGIN BATTLE SPRITE TEST PRINT\n")

    for sprite in battle_sprite_dict:
        print(color_text(sprite, "cyan"))
        for line in battle_sprite_dict[sprite].values():
            print(line)
        else:
            print("")


def print_single_battle_sprite(sprite_name: str, sprite_color: str):
    if sprite_name in battle_sprite_dict.keys():
        for line in battle_sprite_dict[sprite_name].values():
            print(color_text(line, sprite_color))
    else:
        raise ValueError("sprite_name string not valid/not a key in battle_sprite_dict")


def print_battle_sprites_side_by_side(
    enemy_sprites: list,
    enemy_color: str,
    protag_sprites: list = None,
    protag_color: str = None,
):
    # Create dictionaries for enemy sprites
    enemy_lines = {key: battle_sprite_dict[key] for key in enemy_sprites}

    # Optional: Initialize protagonist lines only if protag_sprites is provided
    protag_lines = (
        {key: battle_sprite_dict[key] for key in protag_sprites} if protag_sprites else {}
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
