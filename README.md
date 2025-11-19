# **Virtual AI Hand-Gesture Mouse**

<!-- Project Title Banner -->

<!-- Badges -->

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Integrated-red)

### Developed by **Ansh Soni**

🔗 **LinkedIn:** [https://www.linkedin.com/in/anshs-dev](https://www.linkedin.com/in/anshs-dev)
💻 **GitHub:** [https://github.com/anshs-dev](https://github.com/anshs-dev)

---

## ⭐ Overview

**Virtual Mouse** is an AI-powered hand-gesture system that lets you control your computer without touching a physical mouse. Using **MediaPipe**, **OpenCV**, and **Python**, it tracks your hand in real-time to perform smooth cursor control, scrolling, and clicking.

---

## 🚀 Features

* **🎯 Accurate Cursor Control**
  Control the cursor using your index finger with adaptive smoothing.

* **👍 Gesture-Based Scrolling**

  * **Thumb Up** → Scroll Down
  * **Thumb + Index** → Scroll Up

* **👆 Touch-Free Clicking**

  * **Index + Middle (0.25 sec)** → Left Click
  * **Index + Middle + Ring** → Right Click
    Includes automatic click cooldown to avoid accidental double-clicking.

* **🔒 Single Operation Mode**
  Ensures only one action (move, scroll, or click) runs at a time.

---

## 🧠 How It Works

* Uses **MediaPipe Hands** to detect 21 hand landmarks
* Identifies which fingers are raised to classify gestures
* Maps index fingertip to screen for cursor movement
* Uses smoothing filters for stable pointer motion
* Executes system mouse events through **pynput**

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* Pynput

---

## 📦 Installation

Install dependencies:

```bash
pip install opencv-python mediapipe pynput pyautogui
```

Clone the repository:

```bash
git clone https://github.com/anshs-dev/virtual_mouse
cd virtual_mouse
```

Run the virtual mouse:

```bash
python virtual_mouse.py
```

---

## 🧩 Usage

Use these gestures in front of your webcam:

| Gesture                | Action      |
| ---------------------- | ----------- |
| Index Finger Only      | Move Cursor |
| Thumb Up               | Scroll Down |
| Thumb + Index          | Scroll Up   |
| Index + Middle (0.25s) | Left Click  |
| Index + Middle + Ring  | Right Click |

---

## 🎥 Demo

(Add GIF or project demo link here)

---

## 🚧 Future Enhancements

* Settings panel for gesture customization
* Kalman filter for ultra-smooth pointer movement
* On-screen gesture overlay
* Windows .exe application build

---

## 👨‍💻 Author

**Ansh Soni**
🔗 LinkedIn: [https://www.linkedin.com/in/anshs-dev](https://www.linkedin.com/in/anshs-dev)
💻 GitHub: [https://github.com/anshs-dev](https://github.com/anshs-dev)

---
