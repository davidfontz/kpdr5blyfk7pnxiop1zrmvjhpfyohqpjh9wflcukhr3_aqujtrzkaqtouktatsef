def on_gesture_shake():
    basic.show_string("HI")
    basic.show_leds("""
        . # . . #
        # # # . #
        # # # # #
        . # # # #
        . . # # .
        """)
    basic.show_leds("""
        . # . . #
        # # # . #
        # # # # #
        . # # # #
        . . # # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_string("... ..")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    music.play(music.string_playable("B - B - B - B - ", 1000),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("- - - - B - B - ", 1000),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("- - - - - - - - ", 1000),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
