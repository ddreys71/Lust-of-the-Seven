# Système équipement + inventaire
init python:
    # Items exemples (extensible dans data/items.rpy plus tard)
    items = {
        'potion': {'type': 'consumable', 'hp_restore': 50, 'value': 20},
        'iron_sword': {'type': 'weapon1', 'str_bonus': 5, 'value': 100},
        'leather_armor': {'type': 'body', 'vit_bonus': 3, 'value': 80},
        'fire_amulet': {'type': 'amulet', 'mag_bonus': 8, 'value': 150},
    }
    inventory = ['potion', 'iron_sword', 'leather_armor']  # Start items

    # Équipement MC (dict de slots)
    equipment = {
        'head': None,
        'body': None,
        'weapon1': None,
        'weapon2': None,
        'relic1': None,
        'relic2': None,
        'amulet': None,
    }

    # Stats base MC + calculs
    player_str = 10
    player_mag = 10
    player_vit = 10
    player_agi = 10
    player_luck = 10

    def calculate_stats():
        global player_str, player_mag, player_vit, player_agi, player_luck
        bonuses = {'str': 0, 'mag': 0, 'vit': 0, 'agi': 0, 'luck': 0}
        for slot, item_name in equipment.items():
            if item_name and item_name in items:
                item = items[item_name]
                if 'str_bonus' in item: bonuses['str'] += item['str_bonus']
                if 'mag_bonus' in item: bonuses['mag'] += item['mag_bonus']
                if 'vit_bonus' in item: bonuses['vit'] += item['vit_bonus']
                # Ajoute agi/luck si besoin
        player_str = 10 + bonuses['str']  # Base + bonus
        player_mag = 10 + bonuses['mag']
        player_vit = 10 + bonuses['vit']
        # HP update
        global player_maxhp
        player_maxhp = 150 + (player_vit * 15)

    $ calculate_stats()  # Appel initial