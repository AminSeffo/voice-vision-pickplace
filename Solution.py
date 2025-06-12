import time
import os
import speech_recognition as sr
from pynput import keyboard
from pyniryo import *

# Voice recognition and microphone initialization
recognizer = sr.Recognizer()
microphone = sr.Microphone()
IP_address = "192.168.0.103"

# Connecting to the robot
robot = NiryoRobot(IP_address)
robot.update_tool()
robot.clear_collision_detected()
robot.calibrate_auto()

workspace_name = "amin_home"
text = ""
should_listen = False
should_quit = False

# Voice recognition function
def listen_and_recognize():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Listening...')
        audio = recognizer.record(source, duration=5)
        print("Recognizing...")
        try:
            text_rec = recognizer.recognize_google(audio)
            print("You said:", text_rec)
            return text_rec.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Speech recognition error:", e)
        return ""

# Keyboard event handlers
def on_press(key):
    global should_listen, should_quit
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            should_listen = True
        elif key.char == 'q':
            should_quit = True
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop
while True:
    if should_quit:
        print("Quitting the program")
        robot.close_connection()
        os._exit(0)

    if should_listen:
        should_listen = False
        text = listen_and_recognize()
        robot.move(JointsPosition(-0.0007288597570993538, 0.44790080039177466, -0.4689061703296302, 0, -1.5892967498393173, -0.0014413271980928677))  # observation pose

        if text == "red circle":
            print("Command recognized: red circle")
            try:
                obj_found, shape, color = robot.vision_pick(
                    workspace_name,
                    shape=ObjectShape.CIRCLE,
                    color=ObjectColor.RED
                )
                if obj_found:
                    print("Red circle detected and picked.")
                    # You can add move/place commands here if needed
                    robot.release_with_tool()
                    time.sleep(3)
                else:
                    print("No Red circle detected.")
            except NiryoRobotException as e:
                print(f"vision_pick failed: {e}")

    time.sleep(0.1)  # reduce CPU usage
