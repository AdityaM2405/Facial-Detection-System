# Facial-Detection-System
This is a basic facial detection system which uses OpenCV and PySerial along with an Arduino Uno R3
microcontroller to give a serial output upon detecting a face through a laptop webcam. This has various
applications, such as energy management in smart home systems.

# How it Works
The Python program checks for faces to detect using the computer's webcam. When a face is detected,
a HIGH signal is sent to the connected Arduino board which will then activate the module connected 
to the relay pin on the board.

# Requirements
*Libraries*: OpenCV and PySerial, which can be installed using pip.<br />
*Software*: VSCode or any code writer or IDE, Arduino IDE.<br />
*Hardware*: Arduino Uno R3 or similar microcontroller.<br />

# Setup
*Uploading the Arduino Code*: Connect the Arduino Uno R3 microcontroller to your laptop/PC with a 
USB cable. Then, using the Arduino IDE, write and upload the Arduino code to the Arduino board.<br />
*Hardware Configuration*: Connect an LED to the Arduino board through relay pin 7.<br />
*Running the Python Program*: With the Arduino board connected to your computer, run the Python
program. In line 6 of the program, change the port name from 'COM5' to the appropriate port, 
if necessary.
