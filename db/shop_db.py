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
                "archer": [
                    archer_weapons["Royal Guard's Training Bow"],
                    archer_weapons["Proven Hunter's Bow"],
                ],
                "swordsman": [
                    swordsman_weapons["Royal Guard's Training Sword"],
                    swordsman_weapons["Self-Defense Blade"],
                ],
                "magician": [
                    magician_weapons["Court Magician Apprentice Wand"],
                    magician_weapons["Spell-Caster 1000"],
                ],
            }
        },
        "qurios": {"items": [quest_items["Handmade Doll"]]},
    },
    "lushgrove": {},
    "cinderdune": {},
    "riverfall": {},
    "ember_mountain": {},
    "null_realm": {},
}
