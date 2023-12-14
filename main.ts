basic.showLeds(`
    # # # # #
    . # . # .
    # # # # #
    . # . # .
    # # # # #
    `)
basic.showString("vizer game")
basic.forever(function () {
    basic.showArrow(ArrowNames.NorthEast)
})
