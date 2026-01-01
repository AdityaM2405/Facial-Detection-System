import cv2
import time
import serial

# Connect to Arduino (adjust COM port as needed)
arduino = serial.Serial('COM5', 9600)  # Change COM3 to your Arduino port
time.sleep(2)  # Wait for connection

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
no_person_timer = None
cutoff_delay = 3 # 5 minutes = 300 seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    persons = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(persons) > 0:
        print("Person Detected")
        no_person_timer = None
        arduino.write(b'1')  # Send "ON" signal to Arduino
    else:
        print("No Person")
        if no_person_timer is None:
            no_person_timer = time.time()
        elif time.time() - no_person_timer > cutoff_delay:
            print("Turning OFF AC")
            arduino.write(b'0')  # Send "OFF" signal to Arduino

    cv2.imshow("Room Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()