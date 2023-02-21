for index in range(4):
    basic.show_leds("""
        . # . # .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.pause(1000)
    led.enable(False)
    basic.pause(1000)
    led.enable(True)
    basic.show_leds("""
        . # . # .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
    """)
    led.enable(True)
    basic.show_leds("""
        . # # # .
                . # . # .
                . # . # .
                . # . # .
                . # # # .
    """)
    led.enable(False)
    led.enable(True)
    basic.show_leds("""
        . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # #
    """)
    led.enable(False)
    led.enable(True)
    basic.show_leds("""
        . # # # .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
    """)
    led.enable(False)
    basic.pause(500)