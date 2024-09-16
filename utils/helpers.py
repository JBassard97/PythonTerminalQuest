import os
import sys
import keyboard

def clear_terminal():
    if sys.platform.startswith("win"):
        os.system("cls") # For Windows
    else:
        os.system("clear") # For Mac/Linux

def add_vertical_spaces(count: int):
    for i in range(count):
        print("")

def color_text(text: str, color: str):
    color_codes = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "cyan": "\033[36m",
        # Add other colors as needed
    }
    
    if color not in color_codes:
        raise ValueError("Unsupported color")
    
    ansi_code = color_codes[color]
    reset_code = "\033[0m"
    
    return f"{ansi_code}{text}{reset_code}"

def wait_for_space_press():
    print(f"{color_text('Press SPACE to continue', 'green')}")
    print(f"{color_text('       OR', 'blue')}")
    print(f"{color_text('Press ESC to quit', 'red')}")

    while True:
        event = keyboard.read_event()
        pressed_key = event.name

        if event.event_type == keyboard.KEY_DOWN:
            
            if pressed_key == "esc":
                print(f"{color_text('Exiting...', 'blue')}")
                sys.exit() # Leave Game
            elif pressed_key == "space":
                return # Continue Game


    
    