# Virtual Mouse by Ansh Soni
# LinkedIn: www.linkedin.com/in/anshs-dev
# GitHub: github.com/anshs-dev

import cv2
import mediapipe as mp
import time
import math
import pyautogui
from pynput.mouse import Controller, Button

MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE  = 0.7
CLICK_HOLD_TIME = 0.25
CLICK_COOLDOWN = 0.25
SCROLL_SPEED = 3
BASE_ALPHA = 0.25
MAX_ALPHA = 0.75
SPEED_ALPHA_SCALE = 800.0
DEADZONE_PIXELS = 2
MAX_HANDS = 1

mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils
mouse = Controller()
SCREEN_W, SCREEN_H = pyautogui.size()

def finger_up(lm, tip_id, pip_id):
    return lm[tip_id].y < lm[pip_id].y - 0.02

def thumb_up_fixed(lm):
    tip = lm[4]
    wrist = lm[0]
    return abs(tip.x - wrist.x) > 0.10

filtered_x = SCREEN_W // 2
filtered_y = SCREEN_H // 2
click_hold_start = None
last_click_time = 0.0
last_action = "idle"

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=MAX_HANDS,
                    min_detection_confidence=MIN_DETECTION_CONFIDENCE,
                    min_tracking_confidence=MIN_TRACKING_CONFIDENCE) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        action = "idle"
        perform_move = perform_scroll_up = perform_scroll_down = False
        perform_left_click = perform_right_click = False

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            lm = hand.landmark

            index  = finger_up(lm, 8, 6)
            middle = finger_up(lm, 12,10)
            ring   = finger_up(lm, 16,14)
            pinky  = finger_up(lm, 20,18)
            thumb  = thumb_up_fixed(lm)

            if index and middle and ring and not thumb:
                if time.time() - last_click_time >= CLICK_COOLDOWN:
                    perform_right_click = True
                    action = "right_click"

            elif index and middle and not ring and not thumb:
                if click_hold_start is None:
                    click_hold_start = time.time()
                    action = "hold_start"
                else:
                    if time.time() - click_hold_start >= CLICK_HOLD_TIME:
                        if time.time() - last_click_time >= CLICK_COOLDOWN:
                            perform_left_click = True
                            action = "left_click"
                        click_hold_start = None
                    else:
                        action = "holding"

            else:
                click_hold_start = None

            if thumb and not index and not middle and not ring and not pinky:
                perform_scroll_down = True
                action = "scroll_down"

            elif thumb and index and not middle and not ring and not pinky:
                perform_scroll_up = True
                action = "scroll_up"

            elif index and not thumb and not middle and not ring and not pinky:
                perform_move = True
                action = "move"

            now = time.time()

            if perform_left_click:
                if now - last_click_time >= CLICK_COOLDOWN:
                    mouse.click(Button.left, 1)
                    last_click_time = now
                perform_left_click = False

            if perform_right_click:
                if now - last_click_time >= CLICK_COOLDOWN:
                    mouse.click(Button.right, 1)
                    last_click_time = now
                perform_right_click = False

            if perform_scroll_up:
                mouse.scroll(0, SCROLL_SPEED)

            if perform_scroll_down:
                mouse.scroll(0, -SCROLL_SPEED)

            if perform_move and not perform_scroll_up and not perform_scroll_down:
                tip = lm[8]
                target_x = int(max(0, min(1, tip.x)) * SCREEN_W)
                target_y = int(max(0, min(1, tip.y)) * SCREEN_H)

                dx = target_x - filtered_x
                dy = target_y - filtered_y
                speed = math.hypot(dx, dy)

                alpha = BASE_ALPHA + (speed / SPEED_ALPHA_SCALE)
                alpha = max(0.03, min(alpha, MAX_ALPHA))

                if abs(dx) >= DEADZONE_PIXELS or abs(dy) >= DEADZONE_PIXELS:
                    filtered_x = int(filtered_x + alpha * dx)
                    filtered_y = int(filtered_y + alpha * dy)

                fx = max(0, min(SCREEN_W - 1, filtered_x))
                fy = max(0, min(SCREEN_H - 1, filtered_y))

                try:
                    mouse.position = (fx, fy)
                except:
                    pass

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        else:
            click_hold_start = None
            action = "idle"

        last_action = action
        cv2.putText(frame, f"{last_action}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("AnshS Virtual Mouse", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()
