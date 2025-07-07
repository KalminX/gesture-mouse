# 👆 Gesture Mouse Controller using OpenCV, MediaPipe & PyAutoGUI

Control your computer **mouse pointer** using **hand gestures** via your webcam.
No physical mouse needed — just your fingers.

---

## 🧠 Features

* 🖱️ **Move Cursor** with your **index finger**
* ✅ **Left Click** by pinching **index + thumb**
* ✅ **Right Click** by pinching **pinky + thumb**
* ❌ **Cancel interaction** when any other finger is too close to the thumb
* 🎯 Smooth and responsive cursor tracking
* 🎥 Real-time hand tracking using **MediaPipe**

---

## 🚀 Demo

[https://user-images.githubusercontent.com/your-username/gesture-demo.mp4](https://user-images.githubusercontent.com/your-username/gesture-demo.mp4)
*(Optional: add a screen recording of you using it)*

---

## 🛠️ Tech Stack

| Tech          | Purpose                          |
| ------------- | -------------------------------- |
| **Python**    | Main programming language        |
| **OpenCV**    | Webcam video capture + display   |
| **MediaPipe** | Real-time hand landmark tracking |
| **PyAutoGUI** | Simulate mouse events            |

---

## 📦 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/gesture-mouse-controller.git
   cd gesture-mouse-controller
   ```

2. **Create a virtual environment (optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

---

## ▶️ Run the App

```bash
python gesture_mouse.py
```

Then:

* Point your hand toward the webcam
* Move your **index** to move the cursor
* Pinch **index + thumb** to **left click**
* Pinch **pinky + thumb** to **right click**

---

## 🧠 How It Works

* **MediaPipe Hands** detects **21 hand landmarks**
* **Index finger tip** (`landmark 8`) controls the mouse position
* Distance between fingers is used to detect **pinch gestures**
* If multiple fingers are too close to the thumb, interactions are **cancelled**

---

## ⚙️ Customization

You can modify the gestures by editing the logic in `gesture_mouse.py`:

```python
# Example of changing the pinch threshold:
if distance(index, thumb) < 25:
    pyautogui.click()
```

You could also add:

* ✋ Scroll gestures
* 🤏 Click-and-drag
* 🤚 Multi-hand support

---

## 🧩 File Structure

```
gesture-mouse-controller/
│
├── gesture_mouse.py      # Main script
├── README.md             # This file
└── requirements.txt      # (Optional) pip freeze > requirements.txt
```

---

## 🙏 Acknowledgements

* [MediaPipe by Google](https://google.github.io/mediapipe/)
* [OpenCV](https://opencv.org/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/)

---

## 📜 License

MIT License. Feel free to use and modify it.
