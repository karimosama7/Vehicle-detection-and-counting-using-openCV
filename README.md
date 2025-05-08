# 🚗 Vehicle Counting System using OpenCV

This project is a basic **vehicle counting system** built using **OpenCV** in Python. It detects and counts moving vehicles in a video using **background subtraction** and **contour detection**.

---

## 📹 Demo

The system:

* Detects moving vehicles using `BackgroundSubtractorMOG`
* Draws bounding boxes around vehicles
* Tracks the center of each vehicle
* Counts vehicles as they cross a detection line

---

## 🧠 How It Works

1. **Read video input** using OpenCV.
2. **Convert frames to grayscale** and apply **Gaussian Blur** to reduce noise.
3. Use `cv2.bgsegm.createBackgroundSubtractorMOG()` to extract **foreground mask** (detect motion).
4. **Dilate** the mask to fill gaps and enhance detection.
5. **Find contours** in the mask to detect moving objects.
6. **Draw bounding boxes** and **track centers**.
7. Count vehicles when their center crosses a fixed horizontal line.

---

## 🛠 Requirements

* Python 3.x
* OpenCV

Install required packages:

```bash
pip install opencv-python opencv-contrib-python
```

---

## 📄 Code Example

```python
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 5)
mask = subtracao.apply(blur)
```

---

## 📁 Files

* `video.mp4` – input video file (you can replace it with any traffic video)
* `main.py` – main Python script

---

## 🙏 Acknowledgments

Thanks to **Eng. Ahmed Ibram** for his helpful tutorials and clear explanations.

---

## 📌 Future Improvements

* Add object tracking for more accuracy
* Use deep learning for vehicle classification
* Add entry/exit zone counters


