from db.enemy_db import enemy_data
from db.db_functions import reload_player_data, save_battle_data, clear_battle_db
from utils.helpers import (
    reset_screen,
    color_text,
    add_vertical_spaces,
    press_space_to_continue,
)
from utils.battles.battle_helpers import (
    create_enemies_battle_stats,
    create_enemies_to_fight,
    reset_all_buffs,
)
from utils.battles.random_battle_logic import ask_random_battle_questions

# from assets.sound_effects import play_async_audio


def start_random_battle():

    player_data = reload_player_data()

    # List of possible enemies for the realm the player is in
    enemy_possibilities: list[str] = list(enemy_data[player_data["current_realm"]])
    enemies_to_fight: list[str] = create_enemies_to_fight(enemy_possibilities)

    # ! Creates a list in battle_db storing all stats for each enemy
    save_battle_data(create_enemies_battle_stats(enemies_to_fight))

    reset_all_buffs()
    battle_outcome = ask_random_battle_questions()

    if battle_outcome == "ran away":
        reset_all_buffs()
        clear_battle_db()
        reset_screen()
        print(color_text("You successfully fled the battle!!!", "magenta"))
        add_vertical_spaces(1)
        press_space_to_continue()
    if battle_outcome == "win":
        reset_all_buffs()
        clear_battle_db()
        reset_screen()
        print("You won the battle!")
        add_vertical_spaces(1)
        press_space_to_continue()
    if battle_outcome == "lose":
        reset_all_buffs()
        clear_battle_db()
        reset_screen()
        print(
            color_text(
                player_data["name"] + " is slain and the battle has been lost!", "red"
            )
        )
        add_vertical_spaces(1)
        press_space_to_continue()


# def start_boss_battle(player_data: dict):
#     print("BOSS BATTLE")
