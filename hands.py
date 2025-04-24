def on_received_number(receivedNumber):
    if receivedNumber == 7:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 255, DigitalPin.P12, 0)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 255, DigitalPin.P1, 0)
        basic.pause(5000)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 0, DigitalPin.P12, 0)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 0, DigitalPin.P1, 0)
    elif receivedNumber == 8:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 255, DigitalPin.P12, 1)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 255, DigitalPin.P1, 1)
        basic.pause(5000)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 0, DigitalPin.P12, 1)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 0, DigitalPin.P1, 1)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 255, DigitalPin.P12, 0)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 255, DigitalPin.P1, 0)
    basic.pause(5000)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 0, DigitalPin.P12, 0)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 0, DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 0, DigitalPin.P12, 0)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 0, DigitalPin.P1, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 255, DigitalPin.P12, 1)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 255, DigitalPin.P1, 1)
    basic.pause(5000)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P2, 0, DigitalPin.P12, 1)
    RoboticsWorkshop.dd_mmotor(AnalogPin.P8, 0, DigitalPin.P1, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.SILLY)
radio.set_group(1)
basic.pause(100)
basic.clear_screen()