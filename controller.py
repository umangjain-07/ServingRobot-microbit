def on_received_number(receivedNumber):
    radio.send_number(0)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    radio.send_number(2)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    radio.send_number(7)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    radio.send_number(8)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_sound_loud():
    radio.send_number(9)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_ab():
    radio.send_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(3)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    radio.send_number(1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

radio.set_group(1)
basic.show_icon(IconNames.HOUSE)