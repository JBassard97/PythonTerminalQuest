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
                "At the center of this vast land lies Pythonia Castle: home of the ",
                "cyan",
            )
            + ct("King, ", "blue")
            + ct("Queen, ", "green")
            + ct("and the ", "cyan")
            + ct("Magical Princess.", "yellow"),
            8: ct("Within the catacombs of this marvelous castle lies the ", "cyan")
            + "Diamond of Destiny",
            9: ct(
                "A powerful artifact from the nation's birth that is said to manifest only the desires of the ",
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
            + ct('"Null Realm."', "magenta"),
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
            + ct("don't come back.", "red"),
            15: ct(
                "The Royal Guard has henceforth given the hellhole a second moniker: ",
                "cyan",
            ),
            16: ct('"The Land of No Return"', "magenta"),
            17: ct(
                "Having grown mournfull over the lives lost in the name of protecting Pythonia from some unnamed threat,",
                "cyan",
            ),
            18: ct("the Royal Family ceased any further interactions into the ", "cyan")
            + ct("Null Realm.", "magenta"),
            19: ct(
                "However, this apprehension later became their downfall when the ",
                "cyan",
            )
            + ct("faceless evil ", "red")
            + ct("became all-too-familiar:", "cyan"),
            20: ct("Daemon the Shadow Process", "red"),
            21: ct(
                "A being without tangible form, comprised solely of the malcontent and ill-desires of the entire world.",
                "red",
            ),
            22: ct("In the night, ", "cyan")
            + ct("Daemon ", "red")
            + ct("lauched a ", "cyan")
            + ct("merciless attack ", "red")
            + ct("on Pythonia Castle, in which his militia succeeded in ", "cyan")
            + ct("two awful acts:", "red"),
            23: ct("Pythonia's Queen was ", "cyan")
            + ct("abducted, ", "red")
            + ct("and the ", "cyan")
            + "Diamond of Destiny "
            + ct("was ", "cyan")
            + ct("stolen.", "red"),
            24: ct(
                "After the fray and the pieces of the castle were cleaned up, the saddened King wondered why this had happened.",
                "cyan",
            ),
            25: ct('"Why was my ', "blue")
            + ct("Queen ", "green")
            + ct('the victim when I was clearly the more valuable target?"', "blue"),
            26: ct('"What can this ', "blue")
            + ct("monster ", "red")
            + ct("hope to accomplish with the ", "blue")
            + "Diamond "
            + ct("without its conduit, ", "blue")
            + ct('my Daughter?"', "yellow"),
            27: ct(
                "After holding counsil with his close circle of fellow aristocrats, the King reluctantly made 2 decrees:",
                "cyan",
            ),
            28: ct("The ", "cyan")
            + ct("Magical Princess ", "yellow")
            + ct("shall be kept safe in a slumber until the power of the ", "cyan")
            + "Diamond "
            + ct("is returned to awaken her.", "cyan"),
            29: ct("And...", "yellow"),
            30: ct("Whoever succeeds in this task and is able to defeat ", "cyan")
            + ct("Deamon the Demon Process ", "red")
            + ct("may take my place as King, and I will gladly retire.", "cyan"),
            31: ct(
                "The pair got dressed, filled their bags with anything they thought useful, and set out to begin their adventure...",
                "cyan",
            ),
        }
    }
}
