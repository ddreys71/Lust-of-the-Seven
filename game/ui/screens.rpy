screen main_menu():
    vbox:
        textbutton "Start Game" action Start()
        textbutton "Load" action ShowMenu('load')
        textbutton "Inventory" action ShowMenu('inventory')  # À lier plus tard

screen world_map():
    modal True
    add "images/map_placeholder.jpg"  # Remplace par ton image de ville
    text "Luxuria City" xalign 0.5 yalign 0.1
    imagebutton auto "guild_hotspot_%s.png" action Jump("guild_scene") xpos 200 ypos 300  # Hotspot guilde
    imagebutton auto "shop_hotspot_%s.png" action Jump("shop_scene") xpos 400 ypos 300
    imagebutton auto "forest_hotspot_%s.png" action [Call("enter_combat")] xpos 600 ypos 300  # Combat auto
    textbutton "Back" action Hide("world_map") xalign 1.0 yalign 1.0

screen inventory():
    grid gui.inventory_rows gui.inventory_columns:
        # À étendre avec im.Matrix pour grid items
        text "Inventaire basique (ajoute items ici)"
    textbutton "Equip" action NullAction()  # Lien équipement plus tard

# HUD basique pour affection/currency
screen hud():
    vbox xalign 1.0 yalign 0.0:
        text "Affection: [luxuria.affection]"  # Exemple
        text "Money: [currency['gold']]g [currency['silver']]s [currency['bronze']]b"