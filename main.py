def on_forever():
    led.plot(0, 0)
    basic.pause(2000)
    led.plot(1, 1)
    basic.pause(2000)
    led.plot(2, 2)
    basic.pause(2000)
    led.plot(3, 3)
    basic.pause(2000)
    led.plot(4, 4)
    basic.pause(2000)
    led.unplot(1, 1)
basic.forever(on_forever)
