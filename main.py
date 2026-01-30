import cv2
import mediapipe as mp
import numpy as np
import time
import math
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7,min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
canvas = np.zeros((480, 640, 3), dtype=np.uint8)
prev_x, prev_y = 0, 0
color_list = [(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 0, 255)]
color_index = 0
draw_color = color_list[color_index]
color_changed = False
saved = False
brush_thickness = 5
eraser_radius = 30
def fingers_up(hand):
    fingers = []
    if hand.landmark[4].x < hand.landmark[3].x - 0.04:
        fingers.append(1)
    else:
        fingers.append(0)
    for tip in [8, 12, 16, 20]:
        if hand.landmark[tip].y < hand.landmark[tip - 2].y - 0.04:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers
def distance(point1, point2):
    return math.hypot(point2[0]-point1[0], point2[1]-point1[1])
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    for i, color in enumerate(color_list):
        cv2.rectangle(frame, (i * 160, 0), ((i + 1) * 160, 60), color, -1)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(hand)
            x = int(hand.landmark[8].x * 640)
            y = int(hand.landmark[8].y * 480)
            thumb_x, thumb_y = int(hand.landmark[4].x * 640), int(hand.landmark[4].y * 480)
            brush_thickness = max(3, min(20, int(distance((x, y), (thumb_x, thumb_y)) / 2)))
            if fingers == [1, 0, 0, 0, 0]:
                if not saved:
                    filename = f"air_drawing_{int(time.time())}.png"
                    cv2.imwrite(filename, canvas)
                    print("Saved:", filename)
                    saved = True
                continue
            else:
                saved = False
            if fingers == [1, 1, 1, 1, 1]:
                cv2.circle(frame, (x, y), eraser_radius, (0,0,0), 2)
                cv2.circle(canvas, (x, y), eraser_radius, (0,0,0), -1)
                prev_x, prev_y = 0, 0
                continue
            if fingers == [0, 1, 1, 1, 0]:
                if not color_changed:
                    color_index = (color_index + 1) % len(color_list)
                    draw_color = color_list[color_index]
                    color_changed = True
                continue
            else:
                color_changed = False
            if fingers == [0, 1, 0, 0, 0]:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y
                cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, brush_thickness)
                prev_x, prev_y = x, y
            elif fingers == [0, 1, 1, 0, 0]:
                prev_x, prev_y = 0, 0
            else:
                prev_x, prev_y = 0, 0
    frame = cv2.add(frame, canvas)
    cv2.imshow("Air Writing System", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()