label start:
    scene black
    "Bienvenue dans Lust of the Seven !"
    show screen hud
    "Tu es le MC, prêt pour ton harem adventure."
    call screen world_map

label guild_scene:
    "Tu entres dans la guilde. Luxuria t'attend."
    luxuria "Hey MC, ready for a quest?"
    menu:
        "Accepte la quête":
            "Elle te donne une mission: vaincre des slimes."
            jump enter_combat
        "Flirte":
            $ luxuria.affection += 20
            luxuria "Oh, tu es coquin... +20 affection!"
    return

label shop_scene:
    "Boutique: Achète un item pour 50 bronze."
    $ add_currency(-50, 'bronze')
    "Item acheté!"
    return

label enter_combat:
    "Combat lancé contre Slime Girl!"
    # Appel combat (à coder fully, mais placeholder)
    "Tu gagnes facilement. +50 exp, +15 bronze."
    $ add_currency(15, 'bronze')
    $ luxuria.affection += 10
    if luxuria.affection >= 200:
        jump h_scene_unlocked
    return

label h_scene_unlocked:
    "Scène H débloquée! (Placeholder texte + CG)"
    "Luxuria: 'Viens plus près...' (Insère ton art ici)"
    return