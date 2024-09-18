from .helpers import color_text, add_vertical_spaces, reset_screen

# Returns Capitalized
def ask_name():
    while True:
        name_input = (
            input(f"{color_text('What is your name, adventurer? ', 'cyan')}")
            .strip()
            .capitalize()
        )
        if len(name_input) < 1:  # Entered Nothing
            reset_screen()
            print(
                f"{color_text('Have you no name? Truly you MUST have one...', 'red')}"
            )
            add_vertical_spaces(1)

        elif not name_input.replace(
            " ", ""
        ).isalnum():  # Isn't alphanumeric (allows spaces)
            reset_screen()
            print(f"{color_text('That is not a real name! Be serious!', 'red')}")
            add_vertical_spaces(1)

        else:
            return name_input

# Returns lowercase
def ask_weapon_class():
    weapon_choices = ["swordsman", "archer", "magician"]
    while True:
        weapon_input = (
            input(
                f"{color_text('What weapon class are you starting your journey with?', 'cyan')}\n"
                f"{color_text('Swordsman', 'magenta')}: ({color_text('Attack: Mid', 'blue')},{color_text(' Defense: High', 'green')},{color_text(' Speed: Low', 'red')})\n"
                f"{color_text('Archer', 'magenta')}: ({color_text('Attack: Low', 'red')},{color_text(' Defense: Mid', 'blue')},{color_text(' Speed: High', 'green')})\n"
                f"{color_text('Magician', 'magenta')}: ({color_text('Attack: High', 'green')},{color_text(' Defense: Low', 'red')},{color_text(' Speed: Mid', 'blue')})\n\n"
            )
            .strip()
            .lower()
        )

        if len(weapon_input) < 1:  # Entered Nothing
            reset_screen()
            print(
                f"{color_text('It is dangerous to venture out skill-less! You MUST choose between the three', 'red')}"
            )
            add_vertical_spaces(1)

        elif (
            weapon_input not in weapon_choices
        ):  # If it's not one of the 3 choices (case insensitive)
            reset_screen()
            print(
                f"{color_text('That weapon class is not in the list of choices! Choose from one of the three...', 'red')}"
            )
            add_vertical_spaces(1)

        else:
            return weapon_input

# Returns lowercase
def ask_color():
    color_choices = ["Red", "Blue", "Green", "Cyan", "Magenta", "Yellow"]

    while True:
        for color in color_choices:
            print(color_text(color, color))

        color_input = (
            input(
                f"\n{color_text('What is your favorite color? (This can be changed later)', 'cyan')}\n"
            )
            .strip()
            .lower()
        )

        if len(color_input) < 1:  # It's not doing this for empty inputs
            reset_screen()
            print(
                f"{color_text('Surely one of these colors strikes your fancy?', 'red')}"
            )
            add_vertical_spaces(1)
            continue

        if color_input.lower() in [color.lower() for color in color_choices]:
            return color_input  # Valid input, exit loop and return
        else:
            reset_screen()
            print(
                f"{color_text('That color is not supported in this kingdom!', 'red')}"
            )
            add_vertical_spaces(1)

# Returns lowercase
def ask_companion_type(player_weapon_class: str):
    if player_weapon_class == "swordsman":
        companion_choices = ["dog", "wolf", "bear"]
    if player_weapon_class == "archer":
        companion_choices = ["falcon", "crow", "raven"]
    if player_weapon_class == "magician":
        companion_choices = ["cat", "frog", "lizard", "owl"]

    for companion in companion_choices:
        print(color_text(companion.capitalize(), "magenta"))

    add_vertical_spaces(1)

    while True:
        companion_type_input = (
            input(
                color_text(
                    "Which animal friend will accompany on your journey? ", "cyan"
                )
            )
            .strip()
            .lower()
        )

        if len(companion_type_input) < 1:
            reset_screen()
            print(
                color_text(
                    "Are you heartless? You need a companion in this lonely world...",
                    "red",
                )
            )
            add_vertical_spaces(1)
            continue

        if companion_type_input not in companion_choices:
            reset_screen()
            print(
                color_text(
                    "That animal isn't in the vicinity right now, any other one you like?",
                    "red",
                )
            )
            add_vertical_spaces(1)
            continue

        else:
            return companion_type_input

# Returns Capitalized
def ask_companion_name():
    while True:
        companion_name_input = input(
            color_text("What is you animal friend's name? ", "cyan")
        ).strip().capitalize()
        if len(companion_name_input) < 1:  # Entered Nothing
            reset_screen()
            print(
                color_text(
                    "No name for your buddy? How else will it come when called?", "red"
                )
            )
            add_vertical_spaces(1)
            continue

        elif not companion_name_input.replace(
            " ", ""
        ).isalnum():  # Isn't alphanumeric (allows spaces)
            reset_screen()
            print(color_text("That is not a real name! Be serious!", "red"))
            add_vertical_spaces(1)

        else:
            return companion_name_input
