from picamera2 import Picamera2
import cv2
import mediapipe as mp
import math
import time
import requests

from gpiozero import LED, Buzzer


# ============================================================
# TELEGRAM CONFIGURATION
# ============================================================

BOT_TOKEN = "1086882357:AAF1-GPstN79fQMRSyxPrjbF897MyOdztNw"
CHAT_ID = "-5514259011"

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_telegram_message(message):
    """
    Send a message to Telegram.
    """

    try:
        response = requests.post(
            TELEGRAM_URL,
            data={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        if response.ok:
            print("Telegram notification sent.")
        else:
            print(
                "Telegram error:",
                response.status_code,
                response.text
            )

    except requests.RequestException as error:
        print("Telegram connection error:", error)


# ============================================================
# GPIO
# ============================================================

LED_PIN = 21
BUZZER_PIN = 16

led = LED(LED_PIN)
buzzer = Buzzer(BUZZER_PIN)

# Make sure alarm is OFF at startup
led.off()
buzzer.off()


# ============================================================
# SETTINGS
# ============================================================

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Initial EAR threshold
EAR_THRESHOLD = 0.21

# Eyes must remain closed this long
# before drowsiness is detected.
DROWSINESS_TIME = 2.0


# ============================================================
# MEDIAPIPE EYE LANDMARKS
# ============================================================

LEFT_EYE = [
    362, 385, 387,
    263, 373, 380
]

RIGHT_EYE = [
    33, 160, 158,
    133, 153, 144
]


# ============================================================
# DISTANCE FUNCTION
# ============================================================

def distance(p1, p2):

    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


# ============================================================
# EAR CALCULATION
# ============================================================

def calculate_ear(landmarks, eye_indices, width, height):

    points = []

    for index in eye_indices:

        landmark = landmarks[index]

        x = int(landmark.x * width)
        y = int(landmark.y * height)

        points.append((x, y))

    p1, p2, p3, p4, p5, p6 = points

    horizontal = distance(p1, p4)

    if horizontal == 0:
        return 0.0

    vertical_1 = distance(p2, p6)
    vertical_2 = distance(p3, p5)

    ear = (
        vertical_1 + vertical_2
    ) / (2.0 * horizontal)

    return ear


# ============================================================
# CAMERA
# ============================================================

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration(
    main={
        "size": (
            CAMERA_WIDTH,
            CAMERA_HEIGHT
        ),
        "format": "RGB888"
    }
)

picam2.configure(camera_config)

picam2.start()

time.sleep(2)


# ============================================================
# MEDIAPIPE
# ============================================================

mp_face_mesh = mp.solutions.face_mesh


# ============================================================
# STATE
# ============================================================

eyes_closed_start = None

drowsiness_alert = False

telegram_alert_sent = False


# ============================================================
# STARTUP
# ============================================================

print()
print("==========================================")
print("          SLEEPGUARD AI")
print("==========================================")
print()
print("Camera          : Picamera2")
print("OpenCV          : Enabled")
print("MediaPipe       : Face Mesh")
print("LED             : GPIO 21")
print("Buzzer          : GPIO 16")
print("EAR threshold   :", EAR_THRESHOLD)
print("Drowsiness time :", DROWSINESS_TIME, "seconds")
print("Telegram        : Enabled")
print()
print("Press Q to quit.")
print()


# ============================================================
# MAIN LOOP
# ============================================================

try:

    with mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:

        while True:

            # ------------------------------------------------
            # CAPTURE FRAME
            # ------------------------------------------------

            frame = picam2.capture_array()

            rgb_frame = cv2.cvtColor(
                frame,
                cv2.COLOR_RGB2BGR
            )

            rgb_frame = cv2.cvtColor(
                rgb_frame,
                cv2.COLOR_BGR2RGB
            )

            # ------------------------------------------------
            # MEDIAPIPE PROCESSING
            # ------------------------------------------------

            results = face_mesh.process(rgb_frame)

            display = cv2.cvtColor(
                rgb_frame,
                cv2.COLOR_RGB2BGR
            )

            current_time = time.monotonic()

            # ------------------------------------------------
            # FACE FOUND
            # ------------------------------------------------

            if results.multi_face_landmarks:

                face_landmarks = results.multi_face_landmarks[0]

                h, w, _ = display.shape

                landmarks = face_landmarks.landmark

                # ------------------------------------------------
                # EAR
                # ------------------------------------------------

                left_ear = calculate_ear(
                    landmarks,
                    LEFT_EYE,
                    w,
                    h
                )

                right_ear = calculate_ear(
                    landmarks,
                    RIGHT_EYE,
                    w,
                    h
                )

                ear = (
                    left_ear +
                    right_ear
                ) / 2.0

                # ------------------------------------------------
                # EYE STATE
                # ------------------------------------------------

                eyes_closed = ear < EAR_THRESHOLD

                # ------------------------------------------------
                # DRAW LEFT EYE
                # ------------------------------------------------

                for index in LEFT_EYE:

                    landmark = landmarks[index]

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    cv2.circle(
                        display,
                        (x, y),
                        3,
                        (255, 0, 0),
                        -1
                    )

                # ------------------------------------------------
                # DRAW RIGHT EYE
                # ------------------------------------------------

                for index in RIGHT_EYE:

                    landmark = landmarks[index]

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    cv2.circle(
                        display,
                        (x, y),
                        3,
                        (0, 0, 255),
                        -1
                    )

                # ------------------------------------------------
                # EYES OPEN
                # ------------------------------------------------

                if not eyes_closed:

                    eyes_closed_start = None

                    # Reset alert
                    if drowsiness_alert:

                        led.off()
                        buzzer.off()

                        drowsiness_alert = False

                    # Allow another Telegram alert
                    # for a future drowsiness event.
                    telegram_alert_sent = False

                    status = "AWAKE"
                    status_color = (0, 255, 0)

                    closed_duration = 0.0

                # ------------------------------------------------
                # EYES CLOSED
                # ------------------------------------------------

                else:

                    if eyes_closed_start is None:

                        eyes_closed_start = current_time

                    closed_duration = (
                        current_time -
                        eyes_closed_start
                    )

                    # --------------------------------------------
                    # SHORT EYE CLOSURE
                    # --------------------------------------------

                    if closed_duration < DROWSINESS_TIME:

                        status = "EYES CLOSED"
                        status_color = (0, 255, 255)

                    # --------------------------------------------
                    # DROWSINESS
                    # --------------------------------------------

                    else:

                        status = "DROWSINESS ALERT"
                        status_color = (0, 0, 255)

                        # ----------------------------------------
                        # ACTIVATE GPIO
                        # ----------------------------------------

                        if not drowsiness_alert:

                            led.on()
                            buzzer.on()

                            drowsiness_alert = True

                            print()
                            print(
                                "!!! DROWSINESS DETECTED !!!"
                            )
                            print(
                                "LED ON"
                            )
                            print(
                                "BUZZER ON"
                            )

                        # ----------------------------------------
                        # TELEGRAM
                        # ----------------------------------------

                        if not telegram_alert_sent:

                            message = (
                                "🚨 SLEEPGUARD AI ALERT 🚨\n\n"
                                "Drowsiness detected!\n"
                                "Eyes have been closed for "
                                f"{closed_duration:.1f} seconds.\n\n"
                                f"EAR: {ear:.3f}\n"
                                "LED: ON\n"
                                "Buzzer: ON"
                            )

                            send_telegram_message(message)

                            telegram_alert_sent = True

                # ------------------------------------------------
                # DISPLAY
                # ------------------------------------------------

                cv2.putText(
                    display,
                    "Face detected",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    display,
                    f"EAR: {ear:.3f}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2
                )

                cv2.putText(
                    display,
                    f"Eye status: {status}",
                    (20, 105),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    status_color,
                    2
                )

                # ------------------------------------------------
                # CLOSED TIMER
                # ------------------------------------------------

                if eyes_closed:

                    cv2.putText(
                        display,
                        f"Closed: {closed_duration:.1f}s",
                        (20, 140),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 255, 255),
                        2
                    )

                # ------------------------------------------------
                # ALERT DISPLAY
                # ------------------------------------------------

                if drowsiness_alert:

                    cv2.putText(
                        display,
                        "!!! DROWSINESS ALERT !!!",
                        (90, 190),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0,
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        display,
                        "TELEGRAM ALERT SENT",
                        (140, 225),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 165, 255),
                        2
                    )

            # ------------------------------------------------
            # NO FACE
            # ------------------------------------------------

            else:

                eyes_closed_start = None

                # Turn alarm OFF
                if drowsiness_alert:

                    led.off()
                    buzzer.off()

                    drowsiness_alert = False

                # Reset Telegram state so a future event
                # can send another notification.
                telegram_alert_sent = False

                cv2.putText(
                    display,
                    "No face detected",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )

            # ------------------------------------------------
            # CAMERA WINDOW
            # ------------------------------------------------

            cv2.imshow(
                "SleepGuard AI - Drowsiness Detection",
                display
            )

            # ------------------------------------------------
            # QUIT
            # ------------------------------------------------

            if cv2.waitKey(1) & 0xFF == ord("q"):

                break


# ============================================================
# CLEANUP
# ============================================================

except KeyboardInterrupt:

    print()
    print("Program stopped by user.")


finally:

    led.off()
    buzzer.off()

    picam2.stop()

    cv2.destroyAllWindows()

    print()
    print("LED OFF")
    print("Buzzer OFF")
    print("Camera stopped")
    print("SleepGuard AI stopped.")
