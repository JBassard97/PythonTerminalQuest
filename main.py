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

    print("First, we want to know a little about you to set you on the right path...")
    
    add_vertical_spaces(2)
    
    def ask_name():
        while True:
            name_input = input("What's your name, adventurer?   ")
            if len(name_input.strip()) < 1:
                print("Have you no name? What's REALLY your name?")
                
            elif not name_input.replace(" ", "").isalnum():
                print("That's not a real name! Be serious!")
    
            else:
                return name_input
    
    player_name = ask_name()
    clear_terminal()
    print(f"\n{player_name}? A fitting name for such a warrior!")

    


start_game()

