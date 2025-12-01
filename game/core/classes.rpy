# Classes de base pour le jeu
init python:
    class Character:
        def __init__(self, name, level=1, hp=100, mp=50, str=10, mag=10, agi=10, vit=10, luck=10, affection=0):
            self.name = name
            self.level = level
            self.max_hp = hp + (level * vit)
            self.hp = self.max_hp
            self.max_mp = mp + (level * mag)
            self.mp = self.max_mp
            self.str = str + (level * 1)  # Auto pour waifus, MC manuel
            self.mag = mag
            self.agi = agi  # Détermine ordre tours
            self.vit = vit
            self.luck = luck
            self.affection = affection  # Pour H-scenes
            self.equipment = { 'head': None, 'body': None, 'weapon1': None, 'weapon2': None, 'relic1': None, 'relic2': None, 'amulet': None }
            self.skills = []  # Liste de Skill objects

    class Waifu(Character):
        def __init__(self, name, element, unique_skill, *args, **kwargs):
            super().__init__(name, *args, **kwargs)
            self.element = element  # Feu, Eau, etc.
            self.unique_skill = unique_skill
            self.skills.append(unique_skill)

    class Item:
        def __init__(self, name, type, value, stats_bonus={}):
            self.name = name
            self.type = type  # 'weapon', 'armor', etc.
            self.value = value  # En bronze
            self.stats_bonus = stats_bonus  # {'str': +5}

    class Skill:
        def __init__(self, name, tier, cost_mp, damage_type, power):
            self.name = name
            self.tier = tier  # 1-5
            self.cost_mp = cost_mp
            self.damage_type = damage_type  # 'physical', 'magic', 'elemental'
            self.power = power

# Exemples data (on étendra dans data/)
init python:
    mc = Character("MC", level=1, hp=150, mp=80)  # MC spécial, points manuels
    luxuria = Waifu("Luxuria (Pride)", "Fire", Skill("Pride Flame", 1, 10, "elemental", 25), level=1, hp=120, mp=100, mag=15)

    # Monnaie
    currency = {'gold': 0, 'silver': 0, 'bronze': 100}  # Start avec 100 bronze

    def add_currency(amount, type='bronze'):
        if type == 'bronze':
            currency['bronze'] += amount
            if currency['bronze'] >= 100:
                currency['silver'] += currency['bronze'] // 100
                currency['bronze'] %= 100
        # Etc. pour silver/or

    # Fonction level up simple
    def level_up(char):
        char.level += 1
        char.max_hp += char.vit * 10
        char.hp = char.max_hp
        # Pour MC: menu pour répartir 3 points (à coder après)