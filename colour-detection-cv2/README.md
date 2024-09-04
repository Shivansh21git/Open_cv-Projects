# 🎨 Color Detection using OpenCV
This project demonstrates real-time color detection using OpenCV. The application captures video from your webcam, applies Gaussian blur to reduce noise, and filters out colors within a specified range in the HSV color space. It then detects the largest contour area matching the target color and highlights it with a bounding box.

# ✨ Features
🚀 Real-Time Processing: Captures live video feed and processes each frame in real-time.
🌫 Gaussian Blur: Reduces noise for more accurate color detection.
🎨 HSV Color Space: Filters colors based on user-defined HSV limits.
🔍 Contour Detection: Identifies the largest contour corresponding to the specified color and draws a bounding box around it.

# 🛠 How It Works
📷 Capture Video: The application captures video from your webcam.
✨ Apply Gaussian Blur: Noise in the frame is reduced using a Gaussian blur.
🎨 Convert to HSV: The blurred image is converted from BGR to HSV color space.
🔍 Color Filtering: Colors outside the defined HSV limits are filtered out, leaving only the target color.
📏 Contour Detection: The program finds contours in the filtered image, selects the largest one, and draws a bounding box around it.

# 💻 Installation
Clone the repository:
Copy code
git clone https://github.com/your-username/color-detection-opencv.git
Install the required dependencies:
Copy code
pip install opencv-python numpy

# ▶️ Usage
Run the Python script:
Copy code
python color_detection.py

🎨 Adjust the HSV values inside the script to detect the desired color range.

# ⚙️ Customization
🎯 Change Target Color: Modify the colour variable in the script to change the target color for detection.
🔧 Adjust HSV Limits: Tweak the lLimit and uLimit values in the climt() function for precise color filtering.

# 🤝 Contributions
Contributions are welcome! Feel free to submit a pull request with any improvements or bug fixes
