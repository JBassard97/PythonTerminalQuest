# MEETING WISE WITCH DIALOGUE

from utils.helpers import (
    color_text,
    reset_screen,
    press_space_to_continue,
    add_vertical_spaces,
)
from db.db_functions import reload_player_data, save_player_data
from utils.battles.battles import start_random_battle
from utils.battles.battle_helpers import hundred_percent_player_and_companion_health
from lore.dialogue_dict import dialogue_dict
from lore.dialogue_helpers import (
    print_large_sprite_with_buffer,
    print_multiple_dialogues,
)
from utils.shop_logic import ask_go_shopping, ask_which_shop, go_to_shop


def dialogue_series_1_part_2():
    dialogue_portion = dialogue_dict["series_1"]["part_2"]

    reset_screen()
    print_multiple_dialogues(dialogue_portion, 1, 3)
    add_vertical_spaces(1)
    print_multiple_dialogues(dialogue_portion, 3, 5)
    add_vertical_spaces(1)
    # ! Ask if they want to go shopping
    shopping_decision = ask_go_shopping()
    reset_screen()
    if shopping_decision:
        print(dialogue_portion["5b"])
        add_vertical_spaces(1)
        press_space_to_continue()
        reset_screen
        ask_which_shop()
        reset_screen()
        print(dialogue_portion["5c"])
        add_vertical_spaces(1)
    else:
        print(dialogue_portion["5a"])
        add_vertical_spaces(1)
    print(dialogue_portion[6])
    add_vertical_spaces(1)
    press_space_to_continue()
    # ! Back to story, they walk through the town to the Wise Witch's place

    # print("AHHHH SPIDERS!")
    # press_space_to_continue()
    # start_random_battle()
    # reset_screen()
    # print("AHH EVEN MORE!")
    # start_random_battle(["spider", "rat"])
    # reset_screen()
    # print(
    #     "thanks for killing the spiders. I'll replenish your health and give you some money and potions"
    # )

    player_data = reload_player_data()
    hundred_percent_player_and_companion_health()
    player_data["battles_completed_in_realm"] = 0
    # player_data["current_realm"] = "lushgrove"
    # player_data["current_funds"] += 300
    # player_data["item_inventory"] += ["potion", "potion+", "potion++"]
    # player_data["completed_stories"].append("met_wise_witch")
    save_player_data(player_data)

    # add_vertical_spaces(1)
    # press_space_to_continue()
