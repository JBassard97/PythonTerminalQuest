from utils.logo import print_logo
from utils.helpers import (
    clear_terminal,
    add_vertical_spaces,
    wait_for_space_press,
    color_text,
    reset_screen,
)
from utils.start_questions import (
    ask_name,
    ask_weapon_class,
    ask_color,
    ask_companion_type,
    ask_companion_name,
)


def start_game():
    clear_terminal()
    print(f"\n{color_text('Welcome to...', 'cyan')}\n")
    print_logo()
    add_vertical_spaces(2)
    wait_for_space_press()
    get_player_info()


def get_player_info():
    reset_screen()
    print(
        f"{color_text('First, we want to know a little about you to set you on the right path...', 'magenta')}"
    )
    add_vertical_spaces(1)
    player_name = ask_name()
    reset_screen()
    print(f"{color_text(player_name + '? Great to have you!', 'green')}")
    add_vertical_spaces(1)
    player_weapon_class = ask_weapon_class()
    reset_screen()
    print(
        f"{color_text(f'{player_weapon_class.capitalize()}, eh? May your skills be strong and wise!', 'green')}"
    )
    add_vertical_spaces(1)
    player_color = ask_color()
    reset_screen()
    print(
        color_text(player_color.capitalize(), player_color) + " is a wonderful color!"
    )
    add_vertical_spaces(1)
    player_companion_type = ask_companion_type(player_weapon_class)
    reset_screen()
    print(
        color_text(
            "I pray that you'll take care of your "
            + player_companion_type
            + " companion, and that they'll care for you!",
            "green",
        )
    )
    add_vertical_spaces(1)
    print(color_text("And lastly...", "yellow"))
    add_vertical_spaces(1)
    player_companion_name = ask_companion_name()
    reset_screen()
    print(
        color_text(
            f"A {player_companion_type.capitalize()} named {player_companion_name.capitalize()}? How adorable!",
            "green",
        )
    )
    add_vertical_spaces(1)
    print(color_text("So here is what you've told me thus far...", "yellow"))
    add_vertical_spaces(1)
    print(
        f"{color_text('You are a skilled', 'cyan')} {color_text(player_weapon_class, player_color)} {color_text('named', 'cyan')} {color_text(player_name, player_color)}.\n"
        f"{color_text(player_color.capitalize(), player_color)} {color_text('is your favorite color. I will not forget this.', 'yellow')}\n"
        f"{color_text('You are joined on your journey by a', 'cyan')} {color_text(player_companion_type, player_color)} {color_text('named', 'cyan')} {color_text(player_companion_name, player_color)}."
    )


start_game()
