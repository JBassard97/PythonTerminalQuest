from utils.logo import print_logo
from utils.helpers import clear_terminal, add_vertical_spaces, wait_for_space_press, color_text

def start_game():
    clear_terminal()
    print(f"\n{color_text('Welcome to...', 'cyan')}\n")
    print_logo()
    add_vertical_spaces(5)
    wait_for_space_press()
    get_player_info()

def get_player_info():
    clear_terminal()
    add_vertical_spaces(1)

    print(f"{color_text('First, we want to know a little about you to set you on the right path...', 'magenta')}")
    
    add_vertical_spaces(2)
    
    def ask_name():
        while True:
            name_input = input(f"{color_text('What is your name, adventurer? ', 'cyan')}")
            if len(name_input.strip()) < 1:
                print(f"{color_text('Have you no name? What is REALLY your name?', 'red')}")
                
            elif not name_input.replace(" ", "").isalnum():
                print(f"{color_text('That is not a real name! Be serious!', 'red')}")
    
            else:
                return name_input
    
    player_name = ask_name().strip()
    clear_terminal()
    print(f"{color_text(f'{player_name}? Great to have you!', 'green')}")

    


start_game()

