# MEETING WISE WITCH DIALOGUE

from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from db.db_functions import reload_player_data, save_player_data
from db.shop_db import shop_data
from utils.battles.battles import start_random_battle
from utils.battles.battle_helpers import hundred_percent_player_and_companion_health
from lore.dialogue_dict import dialogue_dict
from lore.dialogue_helpers import (
    print_large_sprite_with_buffer,
    print_multiple_dialogues,
)
from lore.series_1.questions import ask_go_shopping


def dialogue_series_1_part_2():
    player_data = reload_player_data()
    dialogue_portion = dialogue_dict["series_1"]["part_2"]

    reset_screen()
    print_multiple_dialogues(dialogue_portion, 1, 5)
    add_vertical_spaces(1)
    shopping_decision = ask_go_shopping()
    reset_screen()
    if shopping_decision:
        print(dialogue_portion["5b"])
        available_shops = shop_data[player_data["current_realm"]].keys()
        print(available_shops)
    else:  #! They Go Shopping $$$
        print(dialogue_portion["5a"])
        add_vertical_spaces(1)
    press_space_to_continue()

    # print("AHHHH SPIDERS!")
    # press_space_to_continue()
    # start_random_battle(["spider"])
    # reset_screen()
    # print("AHH EVEN MORE!")
    # start_random_battle(["spider", "rat"])
    # reset_screen()
    # print(
    #     "thanks for killing the spiders. I'll replenish your health and give you some money and potions"
    # )

    hundred_percent_player_and_companion_health()
    player_data["battles_completed_in_realm"] = 0
    # player_data["current_realm"] = "lushgrove"
    # player_data["current_funds"] += 300
    # player_data["item_inventory"] += ["potion", "potion+", "potion++"]
    # player_data["completed_stories"].append("met_wise_witch")
    save_player_data(player_data)

    # add_vertical_spaces(1)
    # press_space_to_continue()
