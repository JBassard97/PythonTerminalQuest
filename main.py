from dev.dev_funcs import dev_options
from assets.sound_effects import play_async_audio
from utils.logo import print_logo
from utils.helpers import (
    clear_terminal,
    add_vertical_spaces,
    wait_for_space_or_esc,
    color_text,
    reset_screen,
    convert_to_dict,
    graceful_exit,
)
from utils.start_questions import (
    ask_name,
    ask_weapon_class,
    ask_color,
    ask_companion_type,
    ask_companion_name,
    ask_confirmation,
)
from utils.battles.battles import start_random_battle
from db.db_functions import save_player_data, reload_player_data, clear_player_db
from lore.series_1.part_1 import dialogue_series_1_part_1, add_starting_stats
from lore.series_1.part_2 import dialogue_series_1_part_2


def start_game():
    clear_terminal()
    print(f"\n{color_text('Welcome to...', 'cyan')}\n")
    print_logo()
    add_vertical_spaces(2)
    wait_for_space_or_esc()
    reset_screen()
    player_data = reload_player_data()

    if player_data:
        while True:
            print(
                f"{color_text('I see that you are a returning adventurer, would you like to' ,'cyan')} {color_text('continue your quest', 'green')} {color_text('or', 'cyan')} {color_text('start fresh', 'red')}{color_text('?', 'cyan')}\n"
            )
            continue_confirmation = (
                input(color_text("Enter 'Continue' or 'Start Fresh' ", "yellow"))
                .strip()
                .lower()
            )

            if continue_confirmation == "start fresh":
                play_async_audio("decline")
                clear_player_db()
                get_player_info()
                break
            if continue_confirmation == "continue":
                play_async_audio("accept")
                begin_adventure()
                break
            if continue_confirmation == "dev":
                dev_options(player_data)
            else:
                reset_screen()
                continue
    else:
        get_player_info()


def get_player_info():
    while True:
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
            color_text(player_color.capitalize(), player_color)
            + " is a wonderful color!"
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

        final_answers_list: list[str] = [
            player_name,
            player_weapon_class,
            player_color,
            player_companion_type,
            player_companion_name,
        ]

        acceptance_of_fate: bool = ask_confirmation(*final_answers_list)

        if acceptance_of_fate:  # If they confirm the details...
            player_save = convert_to_dict(*final_answers_list)
            save_player_data(player_save)
            begin_adventure()
            break
        else:
            continue


def begin_adventure():
    reset_screen()
    while True:
        # 
        print("at the beginning of begin_adventure()")
        # 
        player_data = reload_player_data()

        if "completed_stories" in player_data.keys():  # If Intro Story Complete...
            if player_data["completed_stories"][-1] == "intro_story":
                dialogue_series_1_part_2()
            if player_data["completed_stories"][-1] == "met_wise_witch":
                print("end of development")
                break

        else:  # Start Intro Story
            dialogue_series_1_part_1(player_data)
            # Start a list of completed story parts
            player_data = add_starting_stats(player_data)
            save_player_data(player_data)
            wait_for_space_or_esc()


start_game()

# start_random_battle()
