basic.show_leds("""
    # # # # #
    . # . # .
    # # # # #
    . # . # .
    # # # # #
    """)
basic.show_string("vizer game")

def on_forever():
    basic.show_arrow(ArrowNames.NORTH_EAST)
basic.forever(on_forever)
