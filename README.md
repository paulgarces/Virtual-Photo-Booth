# 📸 Virtual Photo Booth (Hands-Free with Hand Gestures)

This project allows users to take hands-free photos using **gesture detection** via a webcam. When all five fingers are detected as raised, a 3-second countdown begins, and a photo is captured automatically. Users can then name and save their photos locally.

---

## 🚀 How It Works

- The webcam is initialized and continuously scans for a hand using **MediaPipe**.
- If all 5 fingers are detected as "up" ✋, a 3-second countdown is triggered.
- Once the countdown reaches 0, the app:
  - Prompts the user in the **terminal** to enter a name for their photo.
  - Saves the current frame (photo) in a folder called `Photos/`.
  - Displays "Photo Taken!" on the webcam screen for 1 second.

---

## 🖥️ How to Use

### 1. Install Dependencies

- Make sure you have Python 3 installed. Then run:
    - pip install opencv-python mediapipe

### 2. Run the App

python virtual_photo.py

### 3. Use the App

- Raise your hand with all 5 fingers up ✋.
- Wait for the 3-second countdown.
- When prompted, type a name for your photo in the terminal (no spaces!).
- Your photo will be saved in the Photos/ folder.
- Repeat as many times as you’d like.
- Press q in the webcam window to quit.

⚠️ **Note**: The camera feed will freeze until you enter a title for your photo in the terminal. After entering a name, the app resumes normally and allows you to take more photos.

---

## 📁 Where Are My Photos Saved

All photos are saved in the Photos/ folder located in the same directory as the script.

You can:
- Access them from Finder (Mac) or File Explorer (Windows).
- Open, edit, or download them like regular image files.
