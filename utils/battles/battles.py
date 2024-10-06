from db.enemy_db import enemy_data
from db.item_db import item_data

from utils.battles.battle_helpers import (
    ask_player_choice,
    ask_attack_who,
    ask_which_item,
    ask_use_item_on_who,
    ask_companion_choice,
    create_enemies_to_fight,
    create_enemy_string,
    create_protag_string,
    display_battle,
    battle_play_by_play,
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

    def ask_battle_questions(enemies_to_fight: list, player_data: dict):
        while True:
            display_battle(*display_battle_params)

            # Reset previous choices before asking again
            player_attack_target = None
            item_choice = None
            item_target_choice = None
            companion_choice = None

            player_choice = ask_player_choice()

            if player_choice == "attack":
                if len(enemies_to_fight) == 2:
                    display_battle(*display_battle_params)
                    player_attack_target = ask_attack_who(enemies_to_fight, player_data)
                else:
                    player_attack_target = enemy_data[player_data["current_realm"]][
                        enemies_to_fight[0]
                    ]["display_name"]

            elif player_choice == "defend":
                # Defend logic placeholder
                pass

            elif player_choice == "use item":
                display_battle(*display_battle_params)
                item_choice = ask_which_item(player_data)

                # If player chose to go back, restart question loop
                if item_choice == "back":
                    play_async_audio("decline")
                    continue

                if (
                    item_choice in item_data["heal_items"]
                    or item_choice in item_data["buff_items"]
                ):
                    if len(protags_to_fight) == 2:
                        display_battle(*display_battle_params)
                        item_target_choice = ask_use_item_on_who(
                            item_choice, enemies_to_fight, player_data
                        )
                    else:
                        item_target_choice = player_data["name"]

                if item_choice in item_data["battle_items"]:
                    if len(enemies_to_fight) == 2:
                        display_battle(*display_battle_params)
                        item_target_choice = ask_use_item_on_who(
                            item_choice, enemies_to_fight, player_data
                        )
                    else:
                        item_target_choice = enemy_data[player_data["current_realm"]][
                            enemies_to_fight[0]
                        ]["display_name"]

            elif player_choice == "run away":
                # Run Away logic placeholder
                pass

            # Companion move (if companion is alive)
            if player_data["is_companion_alive"]:
                display_battle(*display_battle_params)
                companion_choice = ask_companion_choice(player_data)

            display_battle(*display_battle_params)

            # Proceed to battle actions
            battle_play_by_play(
                player_data,
                enemies_to_fight,
                player_choice,
                companion_choice,
                player_attack_target,
                item_choice,
                item_target_choice,
            )
            break  # Exit after resolving actions

    ask_battle_questions(enemies_to_fight, player_data)


# def start_boss_battle(player_data: dict):
#     print("BOSS BATTLE")
