# 🖐️ Hand Gesture Controlled LED System
Welcome to the Hand Gesture Controlled LED System repository! This project uses OpenCV and MediaPipe to detect hand gestures and control the state of LEDs accordingly. With a simple and intuitive interface, you can count the number of fingers you're holding up, and the corresponding number of LEDs will light up.

# 🚀 Features
Real-Time Hand Gesture Recognition: Detects and recognizes the number of fingers held up in real-time.
MediaPipe Integration: Leverages the power of Google's MediaPipe for accurate and fast hand landmark detection.
LED Control: Maps hand gestures to control the number of active LEDs.
Customizable: Easily adjust the thresholds for gesture recognition and LED control.

# 🛠️ Installation
Prerequisites
Python 3.x
OpenCV
MediaPipe
(Optional) Hardware setup with LEDs connected to a microcontroller.

# 🤖 Integration with Hardware
For users interested in integrating this with actual LEDs:

Ensure your microcontroller is compatible with Python.
Use GPIO pins to connect the LEDs.
Modify the controller.py file to map gestures to LED control.

# 🌱 Future Enhancements
Support for Multiple Hand Gestures: Add support for more complex gestures to control additional devices.
Wireless Control: Implement a wireless communication protocol (e.g., MQTT) to control devices remotely.
Expand to Other Devices: Beyond LEDs, extend the control to other IoT devices like fans, lights, or even home automation systems.

# 🧑‍💻 Contributing
We welcome contributions! Please feel free to submit issues, fork the repository, and create pull requests.  
