# Paul Garces
# A virtual photo booth allow for users to take hands free photos

# downloading the needed files
import cv2 as cv
import mediapipe as mp
import time
import os

cap = cv.VideoCapture(0) # opens up the default webcam, in this case the laptops
os.makedirs("Photos", exist_ok=True) # making the photo folder
handSolution = mp.solutions.hands # accessing the hands models
hands = handSolution.Hands() # initiliazing the hands models
mp_draw = mp.solutions.drawing_utils # getting the landmarks and drawing the connections, will use later
finger_tips = [4 , 8, 12, 16, 20] 
fingers_up = [] # to store if the fingers are all up, which will be used to start photo countdown

def finger_tracking(landmarkers): # this function is checking which fingers are up and which are down and will return a list
     current_finger_status = [] # list to store the status of each finger in the current frame/one gesture, 1 means the finger is open and up, 0 means the finger is closed (almost like making a fist)
     landmarks = landmarkers.landmark # extracting all the 21 landmark points
     
     if landmarks[finger_tips[0]].x > landmarks[finger_tips[0] - 1].x - 0.01:
        current_finger_status.append(1)
     else:
        current_finger_status.append(0)

    # this is for the rest of the fingers, index (#8), middle (#12), ring (#16), and pinky (#20) (1-5 since we're not including the thumb)
    # since these fingers are vertical, if the tip of the finger is higher (y value) than the fingers PIP (knuckle), then the finger is up (1), if not, then finger is down (0)
    # the value/status of the fingers from this check below is stored to the current_finger_status array
     for i in range(1, 5):
          if landmarks[finger_tips[i]].y < landmarks[finger_tips[i] - 2].y - 0.05:
            current_finger_status.append(1)
          else:
            current_finger_status.append(0)
     return current_finger_status
    # added buffers to each of the checks to make sure the model isn't too sensitive, like shaking or moving the hand too much
    # adds the state of the fingers to the current_finger_status array and returns it
    # this is all done and checked visually

start_time = None
start_countdown = False

if not cap.isOpened():
   ret, frame = cap.read()
   print("Camera not opened")
   exit()

while True:
    ret, frame = cap.read()
    if not ret: # if frame wasn't received, then break and exit
        print("Can't receive frame (stream end?). Exiting")
        break
    
    h, w, _ = frame.shape
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # converting the frame to rgb for mediapip
    results = hands.process(rgb_frame) # processing the frame which was just converted to rgb to the hand model 
    
    if results.multi_hand_landmarks: # this whole section of the if statement is...
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, handSolution.HAND_CONNECTIONS)
            gesture = finger_tracking(hand)
            if sum(gesture) == 5 and not start_countdown: # if all the fingers are up, meaning sum equals 5, and countdown hasn't started ...
                start_countdown = True # basically saying a countdown has started
                start_time = time.time() # records and stores the exact second that countdown began (e.g. 1000.5)
    if start_countdown: # if the countdown has started...
        time_gone = time.time() - start_time # measures how much time has passed since we stored start_time, so now the time since 1000.5 seconds is 1001.8
        countdown = 3 - int(time_gone) # sets countdown timer to 3 seconds minus how many seconds have passed: 1001.8 - 1000.5 = 1.3 -> 3 - 1.3 = 2
        if countdown > 0: # if the countdown is still running, show the number on screen
            cv.putText(frame, f"Taking photo in {countdown}", (50, 100),
                       cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3) # so says "taking photo in 2 seconds"
        else: # if the countdown reaches 0
            photo_title = input("Enter a title for your photo (no spaces): ").strip().replace(" ", "_")
            photo_name = f"Photos/{photo_title}.png"                
            cv.imwrite(photo_name, frame) # saves the current frame
            cv.putText(frame, "Photo Taken!", (50, 100),
                       cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3) # confirmation that the photo was taken
            start_countdown = False # restarts the countdown flag so user can take another photo
            time.sleep(1) # prevents spamming photos by having a 1 second cooldown
    cv.imshow("Virtual Photo Booth", frame) # keeps continously showing the frame
    if cv.waitKey(1) & 0xFF == ord('q'): # if they click q, then the webcam breaks
        break
cap.release()
cv.destroyAllWindows()