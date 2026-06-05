import cv2
import mediapipe as mp
import requests

ESP_IP = "172.20.10.2"

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path='hand_landmarker.task'
    ),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

landmarker = HandLandmarker.create_from_options(options)

def fingers_up(landmarks, w, h):

    lm = [[int(l.x*w), int(l.y*h)] for l in landmarks]

    fingers = []

    fingers.append(
        1 if lm[4][0] < lm[3][0] else 0
    )

    for tip in [8,12,16,20]:
        fingers.append(
            1 if lm[tip][1] < lm[tip-2][1]
            else 0
        )

    return sum(fingers[1:]), fingers[0]

cap = cv2.VideoCapture(0)

gesture_hold = 0
current_gesture = ""
last_triggered = ""

HOLD_FRAMES = 20

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img,1)

    h,w,_ = img.shape

    rgb = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = landmarker.detect(mp_image)

    if result.hand_landmarks:

        for hand in result.hand_landmarks:

            finger_count, thumb = fingers_up(
                hand,w,h
            )

            if finger_count == 0 and thumb == 0:
                gesture = "fist"
            else:
                gesture = str(finger_count)

            cv2.putText(
                img,
                f'Gesture: {gesture}',
                (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

            if gesture == current_gesture:
                gesture_hold += 1
            else:
                current_gesture = gesture
                gesture_hold = 0

            if gesture_hold == HOLD_FRAMES and last_triggered != gesture:

                last_triggered = gesture

                try:

                    if gesture == "1":
                        requests.get(
                            f"http://{ESP_IP}/1"
                        )

                    elif gesture == "2":
                        requests.get(
                            f"http://{ESP_IP}/2"
                        )

                    elif gesture == "3":
                        requests.get(
                            f"http://{ESP_IP}/3"
                        )

                    elif gesture == "4":
                        requests.get(
                            f"http://{ESP_IP}/4"
                        )

                    elif gesture == "fist":
                        requests.get(
                            f"http://{ESP_IP}/off"
                        )

                except:
                    print("ESP32 Not Connected")

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()