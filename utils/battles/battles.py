from db.enemy_db import enemy_data
from utils.helpers import (
    reset_screen,
    color_text,
    add_vertical_spaces,
    press_space_to_continue,
)
from utils.battles.battle_helpers import (
    ask_battle_questions,
    create_enemies_to_fight,
    create_enemy_string,
    create_protag_string,
)
from assets.sound_effects import play_async_audio


def start_random_battle(player_data: dict):

    # List of possible enemies for the realm the player is in
    enemy_possibilities: list[str] = list(enemy_data[player_data["current_realm"]])
    enemies_to_fight: list[str] = create_enemies_to_fight(enemy_possibilities)

    enemy_string: str = create_enemy_string(enemies_to_fight, player_data)

    protags_to_fight: list[str] = [player_data["weapon_class"]]
    if player_data["is_companion_alive"]:
        protags_to_fight.append(player_data["companion_type"])

    protag_string: str = create_protag_string(protags_to_fight, player_data)

    display_battle_params: list = [
        enemy_string,
        protag_string,
        player_data,
        enemies_to_fight,
        protags_to_fight,
    ]

    battle_outcome = ask_battle_questions(
        enemies_to_fight, player_data, display_battle_params
    )

    if battle_outcome == "ran away":
        reset_screen()
        print(color_text("You successfully fled the battle!!!", "magenta"))
        add_vertical_spaces(1)
        press_space_to_continue()


# def start_boss_battle(player_data: dict):
#     print("BOSS BATTLE")
