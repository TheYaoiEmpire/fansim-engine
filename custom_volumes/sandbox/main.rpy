# Define characters

# Always prefix your definitions with {{p}} so they won't conflict with existing resources.

define {{p}}_jo = Character(name="ectoBiologist", kind=pesterchum, what_color='#0715cd', image="john")
# define {{p}}_jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")
define {{p}}_vr = Character(name="arachnidsGrip", kind=trollian, show_blood="cerulean", image="vriska")
define {{p}}_bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", show_blood="olive")

define {{p}}_tz = Character("[tztitle]", kind=trollian, show_blood='teal', image="{{p}}_terezi")

# Give characters poses
# image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)
image {{p}}_terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
# image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image {{p}}_fakemenu = "{{assets}}/fakemenu.png"
image {{p}}_vriskaend = "images/vriska_endcard_badend1.png"
image {{p}}_fakemenu = "{{assets}}/fakemenu.png"

# ob_meulin is already defined; define a new copy using the openround style
define ob_meulin2 = Character(name="MEULIN", show_color="#416600", kind=openround, image="ob_meulin")


# Start of route
# Start of route should always be named like this, where sandbox is replaced
# with your volume_id.
label {{package_entrypoint}}_sandbox:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True

    # Set the scene, fade in from black
    scene bg johnroom

    # Helper for rewind
    "rollback"

    # Test dialogue systems


    bo "Vanilla boldir"
    {{p}}_bo "Custom boldir"
    vr "Vanilla vriska"
    {{p}}_vr "Custom vriska"
    jo "Vanilla john"
    {{p}}_jo "Custom john"
    ob_meulin "Custom openbound"

    show vriska neutral1
    vr "Vanilla vriska"
    {{p}}_vr "Hi! I'm vriska\nLines are loose"
    {{p}}_vr "Hi! I'm vriska, but busy.\nMultiple lines are tight." (show_big=True)
    
    {{p}}_vr "Gray" (show_blood="gray")
    {{p}}_vr "Burgandy" (show_blood="burgandy")
    {{p}}_vr "Bronze" (show_blood="bronze")
    {{p}}_vr "Gold" (show_blood="gold")
    {{p}}_vr "Lime" (show_blood="lime")
    {{p}}_vr "Olive" (show_blood="olive")
    {{p}}_vr "Jade" (show_blood="jade")
    {{p}}_vr "Teal" (show_blood="teal")
    {{p}}_vr "Cerulean" (show_blood="cerulean")
    {{p}}_vr "Indigo" (show_blood="indigo")
    {{p}}_vr "Purple" (show_blood="purple")
    {{p}}_vr "Violet" (show_blood="violet")
    {{p}}_vr "Fuchsia" (show_blood="fuchsia")
    hide vriska

    show boldir neutral
    bo "Vanilla boldir"
    {{p}}_bo "Default"
    {{p}}_bo "Test" (show_blood="test")
    {{p}}_bo "Gray" (show_blood="gray")
    bo "Burgandy" (window_background="gui/textbox_rust.png")
    {{p}}_bo "Burgandy" (show_blood="burgandy")
    bo "Bronze" (window_background="gui/textbox_bronze.png")
    {{p}}_bo "Bronze" (show_blood="bronze")
    bo "Gold" (window_background="gui/textbox_gold.png")
    {{p}}_bo "Gold" (show_blood="gold")
    {{p}}_bo "Lime" (show_blood="lime")
    bo "Olive" (window_background="gui/textbox_olive.png")
    {{p}}_bo "Olive" (show_blood="olive")
    bo "Jade" (window_background="gui/textbox_jade.png")
    {{p}}_bo "Jade" (show_blood="jade")
    bo "Teal" (window_background="gui/textbox_teal.png")
    {{p}}_bo "Teal" (show_blood="teal")
    bo "Cerulean" (window_background="gui/textbox_blue.png")
    {{p}}_bo "Cerulean" (show_blood="cerulean")
    bo "Indigo" (window_background="gui/textbox_cobalt.png")
    {{p}}_bo "Indigo" (show_blood="indigo")
    bo "Purple" (window_background="gui/textbox_purple.png")
    {{p}}_bo "Purple" (show_blood="purple")
    {{p}}_bo "Violet" (show_blood="violet")
    {{p}}_bo "Fuchsia" (show_blood="fuchsia")
    hide boldir


    show john neutral
    jo "Vanilla john"
    {{p}}_jo "Hi! I'm john\nLines are loose"
    {{p}}_jo "Hi! I'm john, but busy.\nMultiple lines are tight." (show_big=True)
    hide john

    # Test our supplemental narrators, characters
    flarp "Flarp instructions."
    narrator_prattle "Generic prattle"
    narrator_dirk "Some ultimate dirk narration."
    narrator_calliope "Narrator calliope"

    # Openbound: Use parameters for effects.
    show ob_meulin idle
    ob_meulin "!!"
    ob_meulin "!!!" (show_hashtags="#hashtag1")
    ob_meulin "A very spooky bit of text which reads about three lines at this size" (show_chuckle=True)
    ob_meulin "spoop" (show_chuckle=True, show_hashtags="#HONK")

    ob_meulin2 "!!"
    ob_meulin2 "!!!" (show_hashtags="#hashtag1")
    ob_meulin2 "HONK" (show_chuckle=True)
    ob_meulin2 "spoop" (show_chuckle=True, show_hashtags="#HONK")
    hide ob_meulin


    # Different approaches to quirk formatting
    show gamzee neutral

    # Approach 1: Call quirksay
    # Arguments are sayer (character), quirk name, text
    $ quirkSay(gam, "gamzee", "Quirk formatting 1")

    # Approach 2: Define a new sayer
    # Define a new character, given an existing character and a quirk
    # New sayer is reusable!
    $ {{p}}gamq = quirkSayer(gam, "gamzee")
    {{p}}gamq "Quirk formatting 2"
    {{p}}gamq "Quirk formatting 2 forever"

    # Approach 3
    # You can quirk format text without saying it directly
    $ gam(quirkSub("gamzee", "Quirk formatting 3") + " and I guess other stuff")
    hide gamzee

    show vriska neutral1
    {{p}}_vr "I'm 8riska"
    hide vriska

    show {{p}}_terezi neutral
    # play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    $ tztitle = "A"
    {{p}}_tz "1"
    $ tztitle = "AAAAAAAAAAAA"
    {{p}}_tz "2"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    {{p}}_tz "3"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    {{p}}_tz "4"
    # Write dialogue!
    {{p}}_tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass

    show {{p}}_fakemenu
    {{p}}_tz "UHHHHHHHH"

    show {{p}}_terezi at right1280 with ease
    {{p}}_tz "*SNIFFFFFFFF*"

    show {{p}}_terezi at left1280 with move
    {{p}}_tz "TF 1S TH1S TH1NG :?"

    hide {{p}}_terezi
    hide {{p}}_fakemenu

    show vriska neutral4

    # Write dialogue!
    vr neutral3 "Hey. Hey. Over here."
    vr ngreen "8itch."

    hide vriska  # goodbye

    # You can also use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("{{p}}_vriskaend", True, True)
    return
