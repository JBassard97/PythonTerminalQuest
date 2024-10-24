import os
import sys
import keyboard
import random
from assets.sound_effects import play_async_audio


# Clears the terminal
def clear_terminal():
    if sys.platform.startswith("win"):
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Mac/Linux


# Adds vertical space according to 'count' param
def add_vertical_spaces(count: int):
    for i in range(count):
        print("")


# Clears terminal and adds a single vertical space for aesthetics
def reset_screen():
    clear_terminal()
    add_vertical_spaces(1)


def graceful_exit():
    play_async_audio("decline")
    sys.exit()


def color_text(text: str, color: str = None, extra: str = None):

    if color is None:
        return text

    color_codes = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "cyan": "\033[36m",
        "magenta": "\033[35m",
        "yellow": "\033[33m",
        # Add other colors as needed
    }

    extra_codes = {"underline": "\033[4m"}

    if color.lower() not in color_codes:
        raise ValueError("Unsupported color value")

    ansi_code = color_codes[color.lower()]
    reset_code = "\033[0m"
    if extra is not None:
        if extra.lower() not in extra_codes:
            raise ValueError("Unsupported extra value")
        extra_code = extra_codes[extra.lower()]
        return f"{extra_code}{ansi_code}{text}{reset_code}"
    else:
        return f"{ansi_code}{text}{reset_code}"


def wait_for_space_or_esc():
    print(f"{color_text('Press SPACE to continue', 'green')}")
    print(f"{color_text('       OR', 'blue')}")
    print(f"{color_text('Press ESC to quit', 'red')}")

    while True:
        event = keyboard.read_event(suppress=True)
        pressed_key = event.name

        if event.event_type == keyboard.KEY_DOWN:

            if pressed_key == "esc":
                play_async_audio("decline")
                print(f"{color_text('Exiting...', 'blue')}")
                sys.exit()  # Leave Game
            elif pressed_key == "space":
                play_async_audio("accept")
                return  # Continue Game


def press_space_to_continue():
    print(color_text("(Press SPACE to continue...)", "yellow"))
    while True:

        event = keyboard.read_event(suppress=True)
        pressed_key = event.name

        if event.event_type == keyboard.KEY_DOWN:
            if pressed_key == "space":
                return


def convert_to_dict(
    player_name: str,
    player_weapon_class: str,
    player_color: str,
    player_companion_type: str,
    player_companion_name: str,
):
    player_save = {
        "name": player_name,
        "weapon_class": player_weapon_class,
        "color": player_color,
        "companion_type": player_companion_type,
        "companion_name": player_companion_name,
    }

    return player_save


def percent_chance_true(percent: int):
    percent = percent / 100
    if random.random() <= percent:
        return True
    else:
        return False
