def print_logo():
    line1 = " _______          _   __                          ___                             _    "
    line2 = "|_   __ \        / |_[  |                       .'   `.                          / |_  "
    line3 = "  | |__) |_   __`| |-'| |--.   .--.   _ .--.   /  .-.  \  __   _   .---.  .--. ` | |-' "
    line4 = "  |  ___/[ \ [  ]| |  | .-. |/ .'`\ \[ `.-. |  | |   | | [  | | | / /__\ \( (`\] | |   "
    line5 = " _| |_    \ '/ / | |, | | | || \__. | | | | |  \  `-'  \_ | \_/ |,| \__., `'.'.  | |,  "
    line6 = "|_____| [\_:  /  \__/[___]|__]'.__.' [___||__]  `.___.\__|'.__.'_/ '.__.'[\__) ) \__/  "
    line7 = "         \__.'                                                                        "

    line_list = [line1,line2,line3,line4,line5,line6,line7]

    colors = ["\033[31m",  # Red
        "\033[33m",  # Orange (Yellow in ANSI)
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[34m",  # Blue
        "\033[35m",   # Violet
        "\033[31m",  # Red
        ]
    
    color_escape = "\033[0m"

    for i, line in enumerate(line_list):
        print(f"{colors[i]}{line}{color_escape}")
