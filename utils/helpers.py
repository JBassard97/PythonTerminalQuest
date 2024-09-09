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

def wait_for_space_press():
    print("Press 'SPACE' to continue")
    print("       OR")
    print("Press 'ESC' to quit")

    while True:
        event = keyboard.read_event()
        pressed_key = event.name

        if event.event_type == keyboard.KEY_DOWN:
            
            if pressed_key == "esc":
                print("Exiting...")
                break # Leave Game
            elif pressed_key == "space":
                return # Continue Game
