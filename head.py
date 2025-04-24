def on_received_number(receivedNumber):
    if receivedNumber == 9:
        for index in range(4):
            pins.servo_write_pin(AnalogPin.P16, 180)
            basic.pause(200)
            pins.servo_write_pin(AnalogPin.P16, 160)
            basic.pause(200)
            pins.servo_write_pin(AnalogPin.P16, 180)
            basic.pause(200)
radio.on_received_number(on_received_number)

basic.show_icon(IconNames.COW)
radio.set_group(1)
pins.servo_write_pin(AnalogPin.P15, 90)
distance = RoboticsWorkshop.ping(DigitalPin.P8, DigitalPin.P1, PingUnit.CENTIMETERS)
basic.pause(1000)
basic.clear_screen()

def on_forever():
    global distance
    distance = RoboticsWorkshop.ping(DigitalPin.P8, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distance < 5:
        for index2 in range(4):
            pins.servo_write_pin(AnalogPin.P15, 90)
            basic.pause(500)
            pins.servo_write_pin(AnalogPin.P15, 120)
            basic.pause(500)
            pins.servo_write_pin(AnalogPin.P15, 90)
            basic.pause(500)
            pins.servo_write_pin(AnalogPin.P15, 60)
            basic.pause(500)
            pins.servo_write_pin(AnalogPin.P15, 90)
            basic.pause(500)
basic.forever(on_forever)
