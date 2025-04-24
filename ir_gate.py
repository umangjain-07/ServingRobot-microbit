ir = 0
basic.show_icon(IconNames.LEFT_TRIANGLE)
pins.servo_write_pin(AnalogPin.P16, 180)
basic.pause(200)
basic.clear_screen()

def on_forever():
    global ir
    ir = pins.digital_read_pin(DigitalPin.P1)
    if ir == 1:
        pins.servo_write_pin(AnalogPin.P16, 90)
        basic.pause(5000)
    else:
        pins.servo_write_pin(AnalogPin.P16, 180)
basic.forever(on_forever)
