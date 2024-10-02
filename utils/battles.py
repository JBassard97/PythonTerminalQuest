from db.enemy_db import enemy_data
from utils.helpers import reset_screen, add_vertical_spaces, color_text
from assets.battle_ascii_sprites import print_battle_sprites_side_by_side
import random

battle_actions = ["Attack", "Defend", "Use Item", "Run"]


def start_random_battle(player_data: dict):
    #! 1 or 2 randomly selected enemies to fight
    def random_enemy_count():
        return random.choice([1, 2])

    # List of possible enemies for the realm the player is in
    enemy_possibilities = list(enemy_data[player_data["current_realm"]])
    enemies_to_fight = []
    for i in range(random_enemy_count()):
        enemies_to_fight.append(random.choice(enemy_possibilities))

    #! Creating enemy description string
    enemy_string = ""
    if len(enemies_to_fight) == 2:  # If there are 2 enemies...
        if enemies_to_fight[0] == enemies_to_fight[1]:  # And they're the same enemy...
            duplicate_enemy = enemies_to_fight[0]
            enemy_string = f"                                2 {enemy_data[player_data['current_realm']][duplicate_enemy]['display_name']}s"
        else:  # 2 enemies and they're different...
            enemy_string = f"                                  {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']} and a {enemy_data[player_data['current_realm']][enemies_to_fight[1]]['display_name']}"
    else:  # There's just one enemy...
        enemy_string = f"          {enemy_data[player_data['current_realm']][enemies_to_fight[0]]['display_name']}"

    #! Creating protagonist list (omitting companion if dead)
    protags_to_fight = [player_data["weapon_class"]]
    if player_data["is_companion_alive"]:
        protags_to_fight.append(player_data["companion_type"])

    #! Creating protag description string
    protag_string = ""
    if len(protags_to_fight) == 2:
        protag_string = f"{player_data['name']} and {player_data['companion_name']}"
    else:
        protag_string = f"{player_data['name']}"

    def print_battle_desc(enemy_string: str, protag_string: str):
        desc_string = f'{color_text(enemy_string, "red")} {color_text("VS", "cyan")} {color_text(protag_string, player_data["color"])}{color_text("!!!", "cyan")}'
        print(desc_string)

    #! Displaying the battle
    reset_screen()
    print_battle_desc(enemy_string, protag_string)
    add_vertical_spaces(1)
    print_battle_sprites_side_by_side(
        enemies_to_fight, "red", protags_to_fight, player_data["color"]
    )


def start_boss_battle(player_data: dict):
    print("BOSS BATTLE")
