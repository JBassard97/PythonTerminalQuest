from utils.helpers import color_text

large_sprite_dict = {
    "daemon_the_shadow_process": {
        "a": r"                                             ,--,  ,.-.       ",
        "b": r"                ,                  \,       '-,-`,'-.' | ._   ",
        "c": r"               /|          \    ,   |\         }  )/  / `-,', ",
        "d": r"              [ ,          |\  /|   | |        /  \|  |/`  ,` ",
        "e": r"              | |       ,.`  `,` `, | |  _,...(   (      .',  ",
        "f": r"              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\.",
        "g": r"               \  \_\,``,   ` , ,  /  |         )         _,/.",
        "h": r"                \  '  `  ,_ _`_,-,<._.<        /         /.   ",
        "i": r"                 ', `>.,`  `  `   ,., |_      |         /.    ",
        "j": r"                   \/`  `,   `   ,`  | /__,.-`    _,   `\.    ",
        "k": r"               -,-..\  _  \  `  /  ,  / `._) _,-\`       \.   ",
        "l": r"                \_,,.) /\    ` /  / ) (-,, ``    ,        |   ",
        "m": r"               ,` )  | \_\       '-`  |  `(               \.  ",
        "n": r"              /  /```(   , --, ,' \   |`<`    ,            |. ",
        "o": r"             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____). ",
        "p": r"       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`        ",
        "q": r"      (-, \           ) \ ('_.-._)/ /,`    /                  ",
        "r": r"      | /  `          `/ \\ V   V, /`     /                   ",
        "s": r"   ,--\(        ,     <_/`\\     ||      /                    ",
        "t": r"  (   ,``-     \/|         \-A.A-`|     /                     ",
        "u": r" ,>,_ )_,..(    )\          -,,_-`  _--`                      ",
        "v": r"(_ \|`   _,/_  /  \_            ,--`                          ",
        "w": r" \( `   <.,../`     `-.._   _,-`                              ",
    },
    "sacred_library": {
        "a": r"                                                |>>>                           ",
        "b": r"                                                |                              ",
        "c": r"                                            _  _|_  _                          ",
        "d": r"                                           |;|_|;|_|;|                         ",
        "e": r"                                           \\.    .  /                         ",
        "f": r"                                            \\:  .  /                          ",
        "g": r"                                             ||:   |                           ",
        "h": r"                                             ||:.  |                           ",
        "i": r"                                             ||:  .|                           ",
        "j": r"                                             ||:   |       \,/                 ",
        "k": r"                                             ||: , |            /`\.           ",
        "l": r"                                             ||:   |                           ",
        "m": r"                                             ||: . |                           ",
        "n": r"              __                            _||_   |                           ",
        "o": r"     ____--`~    '--~~__            __ ----~    ~`---,              ___        ",
        "p": r"-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~",
    },
    "pythonia_castle": {
        "a": r"                                      [\.                                                    ",
        "b": r"                                      |\)                                ____                ",
        "c": r"                                      |                               __(_   )__             ",
        "d": r"                                      Y\          ___               _(          )            ",
        "e": r"                                     T  \       __)  )--.          (     )-----`             ",
        "f": r"                                    J    \   ,-(         )_         `---'                    ",
        "g": r"                                   Y/T`-._\ (     (       _)                 __              ",
        "h": r"                                   /[|   ]|  `-(__  ___)-`  |\          ,-(  __)             ",
        "i": r"                                   | |    |      (__)       J'         (     )               ",
        "j": r"                                   | |  ] |    _           /;\          `-  '                ",
        "k": r"                                  [| |    |    L'         /;  \.                             ",
        "l": r"                                 /||.| /\ |   /\         /.,-._\        ___ _                ",
        "m": r"                                /_|||| || |  /  \        | |{  |       (._.'_)               ",
        "n": r"                      L/\       | \| | '` |_ _ {|        | | U |   /\.                       ",
        "o": r"                     /v^v\/\   `|  Y | [  '-' '--''-''-'-'`'   |   ^v\ /\,\.                 ",
        "p": r"                    / ,'./  \.` |[   |       [     __   L    ] |      /^v\  \.               ",
        "q": r"                    ,'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_           ",
        "r": r"                    --   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y          ",
        "s": r"                       Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-'  _  (^)__  _           ",
        "t": r"                      Y  YY   ;'~~l  |   L     [|\###U'E'\  \ \Y-` _  (^) _Y  _              ",
        "u": r"                     Y  Y Y   ;\~~/\{| [      _,'-\`= = '.\_ ,`   (^)(^) (^) (^)             ",
        "v": r"                         --   ;\~~~/\|  _,.-' _    \_..-'   _ . ,_ Y_ Y_ _Y  _Y__            ",
        "w": r"                        _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^)              ",
        "x": r"                       (^)  (^)`._~ /  L \  _.Y'`  _  ` --  Y - - -(^) - Y - Y -             ",
        "y": r"                        Y    Y    `'--..,-'`      (^)   _  -    _   Y ____                   ",
        "z": r"                          --           _    _ --   Y   (^)   _ (^)  ===   ----               ",
    },
    "world_map": {
        "a": f"                  {color_text('╔════════════════════╗','magenta')}                  ",
        "b": f"                  {color_text('║   The Null Realm   ║','magenta')}                  ",
        "c": f"                  {color_text('║  Land of No Return ║','magenta')}                  ",
        "d": f"                  {color_text('╚══════════╦═════════╝','magenta')}                  ",
        "e": f"                /\ ^ /\ ^ /\ ║ /\ ^ /\ ^ /\                ",
        "f": f" {color_text('╔════════════════╗','red')}/\ ^ /\ ^ ║ ^ /\ ^ /\{color_text('╔════════════════╗','blue')}",
        "g": f" {color_text('║ Ember Mountain ╠','red')}═══╗ ^ /\ ║ /\ ^ ╔═══{color_text('╣   Riverfall    ║','blue')}",
        "h": f" {color_text('╚════════════════╝','red')}   ║ /\ ^ ║ ^ /\ ║   {color_text('╚════════════════╝','blue')}",
        "i": f"        {color_text('╔═══════════╗','cyan')} ╚╦═════╩═════╦╝ {color_text('╔═══════════╗','cyan')}       ",
        "j": f"        {color_text('║  Western  ╠','cyan')}══╣  Pythonia ╠══{color_text('╣  Eastern  ║','cyan')}       ",
        "k": f"        {color_text('║ Barracks  ║','cyan')}  ║   Castle  ║  {color_text('║ Monastary ║','cyan')}       ",
        "l": f"        {color_text('╚═══════════╝','cyan')} ╔╩═════╦═════╩╗ {color_text('╚═══════════╝','cyan')}       ",
        "m": f" {color_text('╔════════════════╗','yellow')}   ║ {color_text('╔════╩════╗','cyan')} ║   {color_text('╔════════════════╗','green')}",
        "n": f" {color_text('║   Cinderdust   ╠','yellow')}═══╝ {color_text('║  South  ║','cyan')} ╚═══{color_text('╣   Lushgrove    ║','green')}",
        "o": f" {color_text('╚════════════════╝','yellow')}     {color_text('║ Caravan ║','cyan')}     {color_text('╚════════════════╝','green')}",
        "p": f"                        {color_text('╚═════════╝','cyan')}                       ",
    },
    "diamond_of_destiny": {
        "a": "                __________________                ",
        "b": "              .-'  \ _.-''-._ /  '-.              ",
        "c": "            .-/\   .'.      .'.   /\-.            ",
        "d": "           _'/  \.'   '.  .'   './  '_            ",
        "e": "          :======:======::======:======:          ",
        "f": "           '. '.  \     ''     /  .' .'           ",
        "g": "             '. .  \   :  :   /  . .'             ",
        "h": "               '.'  \  '  '  /  '.'               ",
        "i": "                 ':  \:    :/  :'                 ",
        "j": "                   '. \    / .'                   ",
        "k": "                     '.\  /.'                     ",
        "l": "                       '\/'                       ",
    },
    "null_realm": {
        "a": r"    .                  .-.    .  __  *     _   .                  ",
        "b": r"           *          /   \     ((       _/ \       *    .        ",
        "c": r"         _    .   .--'\/\_ \     ``     /    \  *   ___           ",
        "d": r"     *  / \_    _/ ^      \/'__        /\/\  /\  __/   \ *        ",
        "e": r"       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .     ",
        "f": r"  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _      ",
        "g": r"     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \.    ",
        "h": r"   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \.   ",
        "i": r"  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.  ",
        "j": r"@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%",
        "k": r"@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%",
        "l": r"@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::",
        "m": r"`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::' ",
        "n": r"`::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'   ",
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
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": "",
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
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": "",
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
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": "",
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
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": "",
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
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": "",
    },
}


def large_sprite_test_print():
    print("\n\nBEGIN LARGE SPRITE TEST PRINT\n")

    for sprite in large_sprite_dict:
        print(color_text(sprite, "cyan"))
        for line in large_sprite_dict[sprite].values():
            print(line)
        else:
            print("")


def print_single_large_sprite(sprite_name: str, sprite_color: str = None):
    if sprite_name in large_sprite_dict.keys():
        for line in large_sprite_dict[sprite_name].values():
            if sprite_color is None:
                print(line)
            else:
                print(color_text(line, sprite_color))
    else:
        raise ValueError("sprite_name string not valid/not a key in large_sprite_dict")
