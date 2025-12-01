label combat_test:
    $ enemy_hp = 100
    $ enemy_maxhp = 100
    scene black
    "Une Slime Girl lubrique t'attaque !"

    label combat_loop:
        menu:
            "Attaque physique":
                $ dmg = renpy.random.randint(20, 30)
                $ enemy_hp -= dmg
                "Tu infliges [dmg] dégâts ! Slime Girl : [enemy_hp]/[enemy_maxhp] HP"
            "Magie de feu (-10 MP)":
                $ dmg = renpy.random.randint(35, 45)
                $ enemy_hp -= dmg
                "Boule de feu ! [dmg] dégâts enflammés !"
            "Fuir":
                "Tu t’enfuis en courant."
                jump after_combat

        if enemy_hp > 0:
            $ enemy_dmg = renpy.random.randint(8, 15)
            "La Slime Girl te touche pour [enemy_dmg] dégâts !"
            jump combat_loop

    "Victoire !"
    $ money_bronze += 40
    $ lux_affection += 35
    "Luxuria gagne 35 points d’affection → [lux_affection]/1000"

    if lux_affection >= 200:
        call h_scene_placeholder

    label after_combat:
        call screen world_map
    return

label h_scene_placeholder:
    scene black with dissolve
    centered "SCÈNE H DÉBLOQUÉE AVEC LUXURIA\n(ton futur CG + texte ultra hot ici)"
    "Elle te plaque contre un arbre et…"
    pause 3.0
    return