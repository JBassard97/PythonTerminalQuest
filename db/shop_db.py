from db.item_db import item_data

quest_items: dict[dict] = item_data["quest_items"]
heal_items: dict[dict] = item_data["heal_items"]
buff_items: dict[dict] = item_data["buff_items"]
battle_items: dict[dict] = item_data["battle_items"]

shop_data = {
    "tutorial": {"Morsel Vendor": {}, "Apothecary": {}, "Armory": {}, "Qurios": {}},
    "lushgrove": {},
    "cinderdune": {},
    "riverfall": {},
    "ember_mountain": {},
    "null_realm": {},
}
