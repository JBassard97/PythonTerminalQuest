from db.item_db import item_data

quest_items: dict[dict] = item_data["quest_items"]
heal_items: dict[dict] = item_data["heal_items"]
buff_items: dict[dict] = item_data["buff_items"]
battle_items: dict[dict] = item_data["battle_items"]
archer_weapons: dict[dict] = item_data["weapons"]["archer"]
swordsman_weapons: dict[dict] = item_data["weapons"]["swordsman"]
magician_weapons: dict[dict] = item_data["weapons"]["magician"]

shop_data = {
    "tutorial": {
        "morsel vendor": {
            "items": [
                heal_items["slice of rosemary bread"],
                heal_items["corn on the cob"],
                heal_items["chicken kabob"],
            ]
        },
        "apothecary": {
            "items": [
                heal_items["potion"],
                heal_items["potion+"],
                buff_items["attack booster"],
                buff_items["defense booster"],
                buff_items["speed booster"],
            ]
        },
        "armory": {
            "items": {
                "weapons": {
                    "archer": [
                        archer_weapons["royal guard's training bow"],
                        archer_weapons["proven hunter's bow"],
                    ],
                    "swordsman": [
                        swordsman_weapons["royal guard's training sword"],
                        swordsman_weapons["hunting blade"],
                    ],
                    "magician": [
                        magician_weapons["court magician apprentice wand"],
                        magician_weapons["spell-caster 1000"],
                    ],
                },
                "other": [battle_items["throwing knife"]],
            }
        },
        "qurios": {"items": [quest_items["handmade doll"]]},
    },
    "lushgrove": {},
    "cinderdune": {},
    "riverfall": {},
    "ember_mountain": {},
    "null_realm": {},
}
