item_data = {
    "quest_items": {
        "Handmade Doll": {
            "description": "A doll made with hair made from horse tails, cute but a little creepy",
            "base_price": 25,
            "resell_price": 20,
        },
        "Golden Crucifix": {
            "description": "A small golden cross adorned with rubies and sapphires, might come in handy later",
            "base_price": 1000,
            "resell_price": 2000,
        },
    },
    "heal_items": {
        #! --------------Medicine------------------
        "potion": {
            "category": "heal_items",
            "description": "Recovers 20 health",
            "heal_value": 20,
            "base_price": 10,
            "resell_price": 7,
        },
        "potion+": {
            "category": "heal_items",
            "description": "Recovers 50 health",
            "heal_value": 50,
            "base_price": 25,
            "resell_price": 20,
        },
        "potion++": {
            "category": "heal_items",
            "description": "Recovers 100 health",
            "heal_value": 100,
            "base_price": 50,
            "resell_price": 40,
        },
        #! ----------------Food-------------------
        "slice of rosemary bread": {
            "category": "heal_items",
            "description": "A single, hearty slice of local rosemary bread, recovers 5 health",
            "heal_value": 5,
            "base_price": 5,
            "resell_price": 2,
        },
        "corn on the cob": {
            "category": "heal_items",
            "description": "Lightly charred in a fire, yet glistening with butter, recovers 10 health",
            "heal_value": 10,
            "base_price": 10,
            "resell_price": 7,
        },
        "chicken kabob": {
            "category": "heal_items",
            "description": "Seasoned chicken chunks on a skewer, recovers 15 health",
            "heal_value": 15,
            "base_price": 15,
            "resell_price": 9,
        },
    },
    "buff_items": {
        "attack booster": {
            "category": "buff_items",
            "description": "A cinnamon-flavored liquid that boosts attack by 25%",
            "attack_boost": 25,
            "base_price": 35,
            "resell_price": 25,
        },
        "defense booster": {
            "category": "buff_items",
            "description": "A orange-flavored liquid that boosts defense by 25%",
            "defense_boost": 25,
            "base_price": 35,
            "resell_price": 25,
        },
        "speed booster": {
            "category": "buff_items",
            "description": "A espresso-flavored liquid that boosts speed by 25%",
            "speed_boost": 25,
            "base_price": 35,
            "resell_price": 25,
        },
    },
    "battle_items": {
        "throwing knife": {
            "category": "battle_items",
            "description": "An aerodynamic blade used to inflict a flat 20 damage",
            "damage_value": 20,
            "base_price": 20,
            "resell_price": 15,
        }
    },
    "weapons": {
        "archer": {
            "Royal Guard's Training Bow": {
                "name": "Royal Guard's Training Bow",
                "description": "A common archery set given to Royal Guard archers on their first day",
                "base_damage": 15,
                "base_price": 50,
                "resell_price": 50,
            },
            "Proven Hunter's Bow": {
                "name": "Proven Hunter's Bow",
                "description": "A bow fit for hunting larger game, like wild boar and deer",
                "base_damage": 20,
                "base_price": 75,
                "resell_price": 75,
            },
        },
        "swordsman": {
            "Royal Guard's Training Sword": {
                "name": "Royal Guard's Training Sword",
                "description": "A common sword and shield set given to Royal Guard swordsmen on their first day",
                "base_damage": 15,
                "base_price": 50,
                "resell_price": 35,
            },
            "Self-Defense Blade": {
                "name": "Self-Defense Blade",
                "description": "A 12-inch blade that is easily concealable, yet perfect for close combat",
                "base_damage": 20,
                "base_price": 75,
                "resell_price": 50,
            },
        },
        "magician": {
            "Court Magician Apprentice Wand": {
                "name": "Court Magician Apprentice Wand",
                "description": "A simple wand made of polished wood given to the apprentices of Court Magicians",
                "base_damage": 15,
                "base_price": 50,
                "resell_price": 35,
            },
            "Spell-Caster 1000": {
                "name": "Spell-Caster 1000",
                "description": 'The first model in the "Spell-Caster" series, perfect for practicing basic magic commands',
                "base_damage": 20,
                "base_price": 75,
                "resell_price": 50,
            },
        },
    },
}
