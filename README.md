# 📸 Virtual Photo Booth (Hands-Free with Hand Gestures)

This project allows users to take hands-free photos using **gesture detection** via a webcam. When all five fingers are detected as raised, a 3-second countdown begins, and a photo is captured automatically. Users can then name and save their photos locally.

All the code and logic for the virtual photo booth is contained in the `virtual_photo.py` file. This is the main script you’ll run to launch the application.

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
    - `pip install opencv-python mediapipe`

### 2. Run the App

```bash
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

---

## 🔐 Privacy

**Each person who uses this script on their own computer will only be able to see their own photos.**
- The Photos/ folder is created locally on their machine.
- Photos are not uploaded or shared.
- The .gitignore ensures that no personal photos are tracked or pushed to GitHub.
