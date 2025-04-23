def on_received_number(receivedNumber):
    if receivedNumber == 0:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 0, DigitalPin.P15, 0)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 0, DigitalPin.P13, 0)
    elif receivedNumber == 1:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 255, DigitalPin.P15, 0)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 255, DigitalPin.P13, 0)
    elif receivedNumber == 2:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 255, DigitalPin.P15, 1)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 255, DigitalPin.P13, 1)
    elif receivedNumber == 3:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 255, DigitalPin.P15, 0)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 255, DigitalPin.P13, 1)
    elif receivedNumber == 4:
        RoboticsWorkshop.dd_mmotor(AnalogPin.P16, 255, DigitalPin.P15, 1)
        RoboticsWorkshop.dd_mmotor(AnalogPin.P14, 255, DigitalPin.P13, 0)
radio.on_received_number(on_received_number)

radio.set_group(1)
basic.show_icon(IconNames.TARGET)
basic.pause(200)
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
