from db.db_functions import reload_player_data, reload_battle_data, clear_battle_db
from db.item_db import item_data
from utils.battles.battle_helpers import (
    create_battle_move_order,
    display_battle,
    move_index_to_word,
    random_companion_attack_target,
    random_enemy_move,
    random_enemy_attack_target,
)
from utils.battles.random_battle_questions import (
    ask_player_choice,
    ask_attack_who,
    ask_which_item,
    ask_use_item_on_who,
    ask_companion_choice,
)
from utils.helpers import color_text, add_vertical_spaces, press_space_to_continue


def ask_random_battle_questions():
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()

    while True:
        display_battle()
        # Reset previous choices before asking again
        player_attack_target = None
        item_choice = None
        item_target_choice = None
        companion_choice = None
        player_choice = ask_player_choice()

        if player_choice == "run away":
            clear_battle_db()
            return "ran away"

        if player_choice == "attack":
            if len(enemy_stats) == 2:
                display_battle()
                player_attack_target = ask_attack_who()
            else:
                player_attack_target = enemy_stats[0]["display_name"]
        elif player_choice == "defend":
            # Defend question placeholder
            pass
        elif player_choice == "use item":
            display_battle()
            item_choice = ask_which_item()
            # If player chose to go back, restart question loop
            if item_choice == "back":
                continue
            if (
                item_choice in item_data["heal_items"]
                or item_choice in item_data["buff_items"]
            ):
                if player_data["is_companion_alive"]:
                    display_battle()
                    item_target_choice = ask_use_item_on_who(item_choice)
                else:
                    item_target_choice = player_data["name"]
            if item_choice in item_data["battle_items"]:
                if len(enemy_stats) == 2:
                    display_battle()
                    item_target_choice = ask_use_item_on_who(item_choice)
                else:
                    item_target_choice = enemy_stats[0]["display_name"]
        # Companion move (if companion is alive)
        if player_data["is_companion_alive"]:
            display_battle()
            companion_choice = ask_companion_choice()
        break

    display_battle()
    # Proceed to battle actions

    battle_outcome = random_battle_play_by_play(
        player_choice,
        companion_choice,
        player_attack_target,
        item_choice,
        item_target_choice,
    )
    # if battle_outcome == "ran away" or battle_outcome is None:
    #     return "ran away"  # Exit on "ran away"
    if battle_outcome:
        return battle_outcome


#! -----------------------------------------------------------------------


def random_battle_play_by_play(
    player_choice: str,
    companion_choice: str = None,  # ? If None, companion is dead
    player_attack_target: str = None,  # ? If None, player isn't attacking
    item_choice: str = None,  # ? If None, player isn't using an item
    item_target_choice: str = None,  # ? If None, item target is implied or isn't using an item
):
    player_data = reload_player_data()
    enemy_stats = reload_battle_data()

    move_order = create_battle_move_order(player_data, enemy_stats)
    same_enemy_index = (
        0  # If 2 similar enemies, this keeps track of which is moving first
    )
    is_player_defending = False
    is_companion_defending = False
    is_enemy_a_defending = False
    is_enemy_b_defending = False

    #! Loop through move_order
    for index, move in enumerate(move_order):

        #! If it's the player's move...
        if "player_name" in move.keys():
            if player_choice == "attack":
                if (
                    player_attack_target == "a" or player_attack_target == "b"
                ):  # If player attacks one of the two same named enemy
                    display_battle()
                    add_vertical_spaces(2)
                    print(
                        color_text(
                            player_data["name"]
                            + " attacks "
                            + enemy_stats[0]["display_name"]
                            + " "
                            + player_attack_target.capitalize()
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )

                else:  # If player attacks one enemy or a unique named enemy
                    display_battle()
                    add_vertical_spaces(2)
                    print(
                        color_text(
                            player_data["name"]
                            + " attacks "
                            + player_attack_target
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )

            if player_choice == "defend":
                display_battle()
                add_vertical_spaces(2)
                print(
                    color_text(
                        player_data["name"] + " defends " + move_index_to_word(index),
                        player_data["color"],
                    )
                )
                is_player_defending = True

            if player_choice == "use item":
                display_battle()
                add_vertical_spaces(2)
                if item_target_choice == "a" or item_target_choice == "b":
                    print(
                        color_text(
                            player_data["name"]
                            + " used the "
                            + item_choice
                            + " on "
                            + enemy_stats[0]["display_name"]
                            + " "
                            + item_target_choice.capitalize()
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )
                else:
                    print(
                        color_text(
                            player_data["name"]
                            + " used the "
                            + item_choice
                            + " on "
                            + item_target_choice
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )

            add_vertical_spaces(1)
            press_space_to_continue()

        #! If it's the companion's move...
        if "companion_name" in move.keys():
            if companion_choice == "attack":
                display_battle()
                add_vertical_spaces(2)
                companion_attack_target = random_companion_attack_target(
                    player_data, enemy_stats
                )
                if companion_attack_target == "a" or companion_attack_target == "b":
                    print(
                        color_text(
                            player_data["companion_name"]
                            + " attacks "
                            + enemy_stats[0]["display_name"]
                            + " "
                            + companion_attack_target.capitalize()
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )

                else:
                    print(
                        color_text(
                            player_data["companion_name"]
                            + " attacks "
                            + companion_attack_target
                            + " "
                            + move_index_to_word(index),
                            player_data["color"],
                        )
                    )

            if companion_choice == "defend":
                display_battle()
                add_vertical_spaces(2)
                print(
                    color_text(
                        player_data["companion_name"]
                        + " defends "
                        + move_index_to_word(index),
                        player_data["color"],
                    )
                )
                is_companion_defending = True

            if companion_choice == "love you":
                display_battle()
                add_vertical_spaces(2)
                print(
                    color_text(
                        player_data["companion_name"]
                        + " chooses to love "
                        + player_data["name"]
                        + " "
                        + move_index_to_word(index),
                        player_data["color"],
                    )
                )

            add_vertical_spaces(1)
            press_space_to_continue()

        #! If it's an enemy's move...
        if "sprite_name" in move.keys():
            enemy_choice = random_enemy_move()
            if enemy_choice == "attack":
                display_battle()
                add_vertical_spaces(2)
                enemy_attack_target = random_enemy_attack_target(player_data)

                # If 2 similar enemies and one is attacking
                if (
                    len(enemy_stats) == 2
                    and enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]
                ):
                    if same_enemy_index == 0:
                        print(
                            color_text(
                                move["display_name"]
                                + " A "
                                + "attacks "
                                + enemy_attack_target
                                + " "
                                + move_index_to_word(index),
                                "red",
                            )
                        )
                        same_enemy_index = 1

                    else:
                        print(
                            color_text(
                                move["display_name"]
                                + " B "
                                + "attacks "
                                + enemy_attack_target
                                + " "
                                + move_index_to_word(index),
                                "red",
                            )
                        )

                else:
                    print(
                        color_text(
                            move["display_name"]
                            + " attacks "
                            + enemy_attack_target
                            + " "
                            + move_index_to_word(index),
                            "red",
                        )
                    )
            if enemy_choice == "defend":
                display_battle()
                add_vertical_spaces(2)
                if (
                    len(enemy_stats) == 2
                    and enemy_stats[0]["display_name"] == enemy_stats[1]["display_name"]
                ):
                    if same_enemy_index == 0:
                        print(
                            color_text(
                                move["display_name"]
                                + " A "
                                + "defends "
                                + move_index_to_word(index),
                                "red",
                            )
                        )
                        is_enemy_a_defending = True
                        same_enemy_index = 1
                    else:
                        print(
                            color_text(
                                move["display_name"]
                                + " B "
                                + "defends "
                                + move_index_to_word(index),
                                "red",
                            )
                        )
                        is_enemy_b_defending = True
                else:
                    print(
                        color_text(
                            move["display_name"]
                            + " defends "
                            + move_index_to_word(index),
                            "red",
                        )
                    )

            add_vertical_spaces(1)
            press_space_to_continue()

    battle_outcome = ask_random_battle_questions()

    if battle_outcome:
        return battle_outcome
