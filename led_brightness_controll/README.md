# ✋ Finger Gap-Based Brightness Control
This project showcases an innovative way to control the brightness of an LED using hand gestures. By measuring the distance between the thumb and index finger using Mediapipe and OpenCV, the brightness of the LED is dynamically adjusted. The project leverages computer vision techniques to provide a touchless and intuitive interface for controlling brightness.

# 🚀 Project Overview
The primary goal of this project is to demonstrate how computer vision can be used to interact with hardware components like LEDs. Using a webcam, the project captures the real-time video feed and identifies the user's hand landmarks. The distance between the thumb and index finger is calculated, and this distance is used to control the brightness of an LED.

# 🌟 Key Features
👋 Real-time Gesture Recognition: Utilizes Mediapipe's hand tracking to identify and track the thumb and index finger.  
💡 Brightness Control: Measures the gap between fingers to adjust the LED brightness in real-time.  
🐍 Python & OpenCV: Implements image processing and gesture recognition in Python using the OpenCV library.  
🔧 Microcontroller Interface: Designed to interface with a microcontroller (like ESP8266) for hardware control.  

# 🛠️ How It Works
🔍 Hand Detection: The system uses Mediapipe to detect hand landmarks from the webcam feed.  
📏 Distance Calculation: The distance between the thumb and index finger is calculated using their coordinates.  
💡 Brightness Adjustment: The calculated distance is sent to a microcontroller, which adjusts the brightness of an LED based on the distance.  
👁️ Visual Feedback: The system provides visual feedback by drawing circles on the thumb and index finger and a line connecting them.  

# 📋 Requirements
Python 3.x 🐍  
OpenCV 📸  
Mediapipe 🖐️  
Microcontroller (e.g., ESP8266) 🔧  
Webcam 📷  
LED for brightness control 💡  

# ⚙️ Installation
Clone this repository:  
Copy code  
git clone https://github.com/yourusername/finger-gap-brightness-control.git  
Install the required Python packages:  
Copy code  
pip install opencv-python mediapipe  

# ▶️ Usage  
Run the Python script:  
Copy code  
python brightness_control.py  
Ensure that your webcam is working and the microcontroller is connected.
Adjust the brightness by changing the distance between your thumb and index finger.

# 🔧 Hardware Integration
The project is designed to work with a microcontroller (like ESP8266) that receives the calculated distance and adjusts the LED brightness accordingly. The microcontroller can be programmed to map the distance to a PWM signal that controls the LED's brightness.

# 🎥 Demo
(Include a screenshot or GIF demonstrating the project in action.)  

# 🌱 Future Enhancements
💡 Support for Multiple LEDs: Extend the functionality to control multiple LEDs or RGB LEDs.  
📱 Mobile Integration: Integrate with a mobile app for remote brightness control.  
🔄 Advanced Gestures: Add support for more complex gestures to control other parameters like color or pattern.  
🤝 Contributing  
Feel free to submit issues or pull requests if you have suggestions for improving this project.
