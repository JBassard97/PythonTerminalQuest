from utils.helpers import color_text


def ask_go_shopping():
    valid_inputs = ["yes", "no"]

    print(color_text("Enter Yes or No:", "yellow"))
    while True:
        shopping_input = input().strip().lower()
        if shopping_input in valid_inputs:
            if shopping_input == "yes":
                return True
            else:
                return False
