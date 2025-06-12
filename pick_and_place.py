#!/usr/bin/env python3
import time
import os
import speech_recognition as sr
from pyniryo import *
from pynput import keyboard

# Voice recognition and microphone initialization
recognizer = sr.Recognizer()
microphone = sr.Microphone()
IP_address = "192.168.0.103"

# Connecting to the robot
robot = NiryoRobot(IP_address)
robot.update_tool()
robot.calibrate_auto()

# Position to be changed
joints_read = robot.get_joints()
pick_position_joint = JointsPosition(-0.049430527204749275, -0.3368411192069237, -0.7203871715909892, -0.06893648186506107, -0.5569276795922806, 0.006228576741335257)
place_position_joint = JointsPosition(-0.238, -0.390, -0.593, -0.063, -0.554, 0.011)

# Flags
text = ""
should_listen = False
should_quit = False

# Function to listen and recognize voice
def listen_and_recognize():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
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

# Key press handler
def on_press(key):
    global should_listen, should_quit
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            should_listen = True
        elif key.char == 'q':
            should_quit = True
    except AttributeError:
        pass

# Start key listener in background
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop
while True:
    if should_quit:
        print("Quitting the program.")
        robot.close_connection()
        os._exit(0)

    if should_listen:
        should_listen = False
        text = listen_and_recognize()

    if text == "play":
        print("Executing pick and place sequence...")
        try:
            robot.clear_collision_detected()
            robot.move(pick_position_joint)
            robot.grasp_with_tool()
            robot.move(place_position_joint)
            robot.release_with_tool()
        except NiryoRobotException as e:
            print("Robot error:", e)
        text = ""  # reset command
        time.sleep(3)
