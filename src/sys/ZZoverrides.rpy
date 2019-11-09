screen main_menu():


    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add "titlesky"

    #add "gui/sun2.png" at titlesun
    #add "gui/lensflare.png" at titleflare
    #add "gui/clouds.png" at titleclouds


    add "gui/title_noglitch" pos(5, 5) at title

    #imagebutton auto "gui/title_%s.png" action NullAction() pos (5, 5)

    imagebutton auto "{{assets_common}}/start_canon_%s.png" action Start("start") pos (20, 285) at menumove
    imagebutton auto "{{assets_common}}/start_fanon_%s.png" action Start("start_custom") pos (20, 345) at menumove
    imagebutton auto "gui/load_%s.png" action ShowMenu('load') pos (20, 405) at menumove
    imagebutton auto "gui/options_%s.png" action ShowMenu('preferences') pos (20, 465) at menumove
    imagebutton auto "gui/friends_%s.png" action ShowMenu('achievements') pos (20, 525) at menumove
    imagebutton auto "gui/credits_%s.png" action ShowMenu('about') pos (20, 585) at menumove
    imagebutton auto "gui/exit_%s.png" action Quit(confirm=not main_menu) pos (20, 645) at menumove

define config.developer = True

define gui.name_xalign = 0.0

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.5
    xpos 0