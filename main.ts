input.onGesture(Gesture.Shake, function () {
    basic.showString("HI")
    basic.showLeds(`
        . # . . #
        # # # . #
        # # # # #
        . # # # #
        . . # # .
        `)
    basic.showLeds(`
        . # . . #
        # # # . #
        # # # # #
        . # # # #
        . . # # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showString("... ..")
})
basic.forever(function () {
    music.play(music.stringPlayable("B - B - B - B - ", 1000), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("- - - - B - B - ", 1000), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("- - - - - - - - ", 1000), music.PlaybackMode.UntilDone)
})
