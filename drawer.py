def on_button_pressed_a():
    global speed
    if speed < 245:
        speed = speed + 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global speed
    if speed < 10:
        speed = speed - 10
input.on_button_pressed(Button.B, on_button_pressed_b)

distanceright = 0
distanceleft = 0
speed = 0
basic.show_icon(IconNames.SWORD)
basic.pause(200)
state_right = 0
stateleft = 0
speed = 75
basic.clear_screen()

def on_forever():
    global distanceleft, distanceright, stateleft, state_right
    distanceleft = RoboticsWorkshop.ping(DigitalPin.P8, DigitalPin.P1, PingUnit.CENTIMETERS)
    distanceright = RoboticsWorkshop.ping(DigitalPin.P2, DigitalPin.P12, PingUnit.CENTIMETERS)
    if distanceleft < 5 and stateleft == 0:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, speed, DigitalPin.P15, 1)
        basic.pause(1000)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 0, DigitalPin.P15, 1)
        stateleft = 1
        basic.pause(700)
    elif distanceleft > 5 and stateleft == 1:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, speed, DigitalPin.P15, 0)
        basic.pause(1500)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 0, DigitalPin.P15, 0)
        basic.pause(1000)
        stateleft = 0
    elif distanceright < 5 and state_right == 0:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, speed, DigitalPin.P13, 0)
        basic.pause(1000)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 0, DigitalPin.P13, 0)
        state_right = 1
        basic.pause(700)
    elif distanceright > 5 and state_right == 1:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, speed, DigitalPin.P13, 1)
        basic.pause(1500)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 0, DigitalPin.P13, 1)
        basic.pause(700)
        state_right = 0
basic.forever(on_forever)
