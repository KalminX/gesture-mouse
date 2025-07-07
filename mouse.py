import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Settings
pyautogui.FAILSAFE = False
screen_width, screen_height = pyautogui.size()
cooldown = 0.6  # seconds

# Capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, model_complexity=0, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Drawing styles
landmark_style = mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=2)
connection_style = mp_draw.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1)

# Time tracking
last_left_click = 0
last_right_click = 0

def distance(p1, p2, frame_w, frame_h):
    x1, y1 = int(p1.x * frame_w), int(p1.y * frame_h)
    x2, y2 = int(p2.x * frame_w), int(p2.y * frame_h)
    return math.hypot(x2 - x1, y2 - y1), (x1, y1), (x2, y2)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    frame_h, frame_w, _ = frame.shape

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS, landmark_style, connection_style)

        # Landmarks
        index_tip = hand.landmark[8]
        middle_tip = hand.landmark[12]
        ring_tip = hand.landmark[16]
        pinky_tip = hand.landmark[20]
        thumb_tip = hand.landmark[4]

        # Cursor movement
        cursor_x = int(index_tip.x * screen_width)
        cursor_y = int(index_tip.y * screen_height)
        pyautogui.moveTo(cursor_x, cursor_y)

        # Check cancelation condition: any finger (except index/pinky) close to thumb
        cancel = False
        for finger_tip in [middle_tip, ring_tip]:
            dist, _, _ = distance(finger_tip, thumb_tip, frame_w, frame_h)
            if dist < 30:
                cancel = True
                break

        if not cancel:
            # Left click: index + thumb
            dist_left, index_pos, thumb_pos = distance(index_tip, thumb_tip, frame_w, frame_h)
            if dist_left < 25 and time.time() - last_left_click > cooldown:
                pyautogui.click(button='left')
                last_left_click = time.time()
                print("Left Click")
                cv2.circle(frame, index_pos, 10, (255, 0, 255), cv2.FILLED)

            # Right click: pinky + thumb
            dist_right, pinky_pos, thumb_pos2 = distance(pinky_tip, thumb_tip, frame_w, frame_h)
            if dist_right < 25 and time.time() - last_right_click > cooldown:
                pyautogui.click(button='right')
                last_right_click = time.time()
                print("Right Click")
                cv2.circle(frame, pinky_pos, 10, (0, 255, 255), cv2.FILLED)

        else:
            cv2.putText(frame, "Interaction Cancelled", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Gesture Mouse - Thumb + Pinky Right Click", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
