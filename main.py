def on_sound_loud():
    strip.show_color(neopixel.rgb(255, 0, 50))
    strip.show()
    basic.pause(10)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_sound_quiet():
    strip.show_color(neopixel.rgb(25, 0, 6))
    strip.show()
    basic.pause(10)
input.on_sound(DetectedSound.QUIET, on_sound_quiet)

roll = 0
strip: neopixel.Strip = None
pins.servo_write_pin(AnalogPin.P0, 90)
pins.servo_write_pin(AnalogPin.P1, 90)
strip = neopixel.create(DigitalPin.P14, 24, NeoPixelMode.RGB)

def on_forever():
    global roll
    roll = input.rotation(Rotation.ROLL)
    if abs(roll) < 80:
        pins.servo_write_pin(AnalogPin.P0, 120)
        pins.servo_write_pin(AnalogPin.P1, 120)
        basic.pause(200)
    elif abs(roll) > 100:
        pins.servo_write_pin(AnalogPin.P0, 60)
        pins.servo_write_pin(AnalogPin.P1, 60)
        basic.pause(200)
    else:
        pins.servo_write_pin(AnalogPin.P0, 110)
        pins.servo_write_pin(AnalogPin.P1, 70)
        basic.pause(200)
basic.forever(on_forever)


