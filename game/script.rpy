label start:
    scene black with dissolve
    centered "LUST OF THE SEVEN\nv0.1"

    # Variables de base
    $ money_gold = 1
    $ money_silver = 23
    $ money_bronze = 45
    $ lux_affection = 0

    show screen hud
    "Tu te réveilles dans la capitale du vice…"
    call screen world_map
    return