from utils.helpers import color_text


# Abbreviated function name to make life easier
def ct(text: str, color: str):
    return color_text(text, color)


dialogue_dict = {
    "series_1": {
        "part_1": {
            1: ct("Welcome to the kingdom of Pythonia...", "green"),
            2: ct(
                "It is a massive sea-surrounded nation comprised of 5 realms.",
                "cyan",
            ),
            3: f'{ct("To the northeast lies ", "cyan")}{ct("Riverfall: ", "blue")}{ct("the freely-flowing source of all fresh water across all 4 realms.", "cyan")}',
            4: f'{ct("To the southeast lies ", "cyan")}{ct("Lushgrove: ", "green")}{ct("the origin of all life and sustenance to be shared equally amongst the inhabitants of Pythonia.", "cyan")}',
            5: f'{ct("To the southwest lies ", "cyan")}{ct("Cinderdust: ", "yellow")}{ct("a vast desert of volcanic ash from the realm above, serving as a burial ground for the departed.", "cyan")}',
            6: f'{ct("To the northwest lies ", "cyan")}{ct("Ember Mountain: ", "red")}{ct("a place of immense power, where all atmospheric warmth emanates from", "cyan")}',
            7: ct(
                "At the center of this vast land lies Pythonia Castle: home of the King, Queen, and the ",
                "cyan",
            )
            + ct("Magical Princess.", "yellow"),
            8: ct("Within the catacombs of this marvelous castle lies the ", "cyan")
            + "Diamond of Destiny",
            9: ct(
                "A powerful artifact from the nation's birth that is said to manifest the desires of the ",
                "cyan",
            )
            + ct("Chosen Maiden", "yellow"),
            10: ct(
                "To the north of Pythonia Castle lies a barren wasteland, completely ",
                "cyan",
            )
            + ct("devoid of life, light, or seemingly anything at all.", "red"),
            11: ct(
                "For this very reason, the Royals of Pythonia only refer to this place as the ",
                "cyan",
            )
            + ct('"Null Realm"', "magenta"),
            12: ct(
                "Despite this observation, every criminal or warlock apprehended by the Royal Guard claims to have had some tie to this place.",
                "cyan",
            ),
            13: ct(
                "Clearly it's hiding something, as it must be a breeding ground for ",
                "cyan",
            )
            + ct("Evil ", "red")
            + ct("under its homey fascade.", "cyan"),
            14: ct(
                "Any investigations into this matter have been met with search parties that simply ",
                "cyan",
            )
            + ct("don't come back", "red"),
            15: ct(
                "The Royal Guard has henceforth given the hellhole a second moniker: ",
                "cyan",
            ),
            16: ct('"The Land of No Return"', "magenta"),
            
        }
    }
}
