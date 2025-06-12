import speech_recognition as sr
from pynput import keyboard
from pyniryo import *

# --- Setup ---
# TODO: Initialize recognizer and microphone


IP_address = "IP_Address"

# TODO: Connect to the robot and perform setup (update tool, clear collision, calibrate)
robot = None  # NiryoRobot(IP_address)

workspace_name = "WORKSPACE"
should_listen = False
should_quit = False

# --- Voice Recognition ---
def listen_and_recognize():
    """
    TODO:
    - Use the microphone to capture voice input
    - Adjust for ambient noise
    - Record audio for a fixed duration (e.g., 5 seconds)
    - Use Google's speech recognition to convert audio to text
    - Handle unknown or failed recognition with error messages
    - Return the recognized text in lowercase
    """
    pass

# --- Keyboard Control ---
def on_press(key):
    """
    TODO:
    - Use pynput to check if CTRL key is pressed → set should_listen = True
    - Check if 'q' key is pressed → set should_quit = True
    - Catch AttributeError for special keys
    """
    pass

# TODO: Start a keyboard listener to monitor key presses
listener = None  # keyboard.Listener(on_press=on_press)

# --- Main Loop ---
while True:
    """
    TODO:
    - If should_quit is True:
        - Close robot connection and exit program
    - If should_listen is True:
        - Reset should_listen
        - Call listen_and_recognize to get command
        - Move robot to a predefined observation pose
        - If command is e.g. "red circle":
            - Use vision_pick to detect and pick the object
            - Handle pick success/failure
            - Optionally add robot actions (e.g., place object, release tool)
            - Handle exceptions like NiryoRobotException
    - Add a small sleep delay to reduce CPU usage
    """
    pass
