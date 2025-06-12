# Vision and Voice Controlled Pick & Place with Ned2 Robot Arm

This project demonstrates a multimodal control system for the **Ned2 6-axis collaborative robot arm**, using both **speech recognition** and **visual object detection** to perform **Pick & Place** tasks.

The robot is controlled via **Python**, with integration of:

- 🎙️ **SpeechRecognition** for voice commands  
- 🎥 **Vision system** of the Ned2 to detect object shapes and colors  
- 🤖 **Pyniryo** SDK for robot control  

---

## Features

✅ Voice-controlled robot operation via microphone  
✅ Visual object recognition (color + shape) with Ned2 camera  
✅ Pick & Place of objects based on user commands  
✅ Safety features (collision handling, emergency quit key)  
✅ Simple keyboard interface to trigger listening  

---

## How It Works

### Workflow:

1. Press `CTRL` key → activates listening mode  
2. Speak a command (e.g. **"red circle"** or **"play"**)  
3. Robot moves to observation pose and detects objects  
4. Robot picks object and places it at predefined location  
5. Press `q` key → safely quits the program  

---

## Example Voice Commands

| Command         | Action                     |
|-----------------|----------------------------|
| `red circle`    | Detect and pick red circle |
| `play`          | Execute Pick & Place demo  |

---

## Setup

### 1️⃣ Requirements

- Python 3.x  
- Ned2 robot connected via IP  
- Camera calibrated in **workspace**  
- Microphone connected to PC  

### 2️⃣ Install Dependencies

```bash
pip install speechrecognition pyniryo pynput
```

### 3️⃣ Run Program


```bash
python3 Solution.py
```

---

## Files

| File             | Purpose |
|------------------|---------|
| `Task.py`        | Task template |
| `Solution.py`    | Full solution with voice + vision control |
| `README.md`      | Project info |

---

## Notes

- Press `CTRL` to start listening → robot awaits command.  
- Press `q` to quit.  
- For visual recognition to work, you must define **workspace name** correctly and position objects clearly within the camera view.  
- Ensure ambient noise is reduced for better speech recognition.

---

## About the Lab

This project is part of the **"Labor Anwendungen der Robotik"** at TUM — focusing on **Pick & Place with Speech and Vision Processing** using the Ned2 platform.
