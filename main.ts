input.onSound(DetectedSound.Loud, function () {
    strip.showColor(neopixel.rgb(255, 0, 50))
    strip.show()
    basic.pause(10)
})
input.onSound(DetectedSound.Quiet, function () {
    strip.showColor(neopixel.rgb(25, 0, 6))
    strip.show()
    basic.pause(10)
})
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P14, 24, NeoPixelMode.RGB)
