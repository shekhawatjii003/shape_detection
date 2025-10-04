**🧠 Real-Time Edge and Contour Detection using OpenCV**

This project uses OpenCV and Python to perform real-time edge detection and contour detection using a webcam feed. It provides a graphical user interface (GUI) with trackbars to adjust Canny Edge thresholds dynamically and visualize results in real-time.
**
📸 Project Overview
**
The project captures live video from your webcam and processes each frame through a series of image processing techniques:

Gaussian Blur – Smooths the image to reduce noise.

Grayscale Conversion – Converts the image to grayscale for edge detection.

Canny Edge Detection – Detects edges using two dynamic threshold values controlled via trackbars.

Dilation – Enhances edges for better contour detection.

Contour Detection – Draws contours around significant shapes in the frame.

Stack Display – Shows all intermediate processing stages in one combined display window.

**🧩 Features**

🔹 Real-time video feed processing

🔹 Adjustable Canny thresholds using trackbars

🔹 Live contour visualization

🔹 Multi-view window display (original, grayscale, edge, contour views)

🔹 Modular functions for image stacking and contour extraction

**🧠 Tech Stack**

Language: Python 3.x

Libraries:

OpenCV (cv2)

NumPy

**⚙️ Installation**

Clone this repository and install dependencies:

git clone https://github.com/yourusername/real-time-contour-detection.git
cd real-time-contour-detection
pip install opencv-python numpy

**▶️ How to Run
**
Connect your webcam.

Run the Python script:

python main.py


Adjust the threshold1 and threshold2 sliders in the PARAMETERS window to fine-tune edge detection.

Press q to quit the program.

📂 File Structure
📁 real-time-contour-detection
├── main.py             # Main source code
├── README.md           # Project documentation
└── requirements.txt    # Dependencies (optional)


You can create a requirements.txt file with:

opencv-python
numpy

**🧩 Function Descriptions**
Function	Description
empty(a)	Placeholder callback for trackbar (required by OpenCV).
getcontours(img, imgcontour)	Detects and draws contours for objects with area > 1000 pixels.
stackImages(scale, imgArray)	Utility function to display multiple image windows in one frame.
🖼️ Output Preview

When you run the script, you’ll see a stacked window showing:

Original Image

Grayscale Image

Canny Edges

Dilated Edges

Contours

💡 Example Use Cases

Object boundary detection

Shape recognition

Edge detection tuning for computer vision projects

**🧑‍💻 Author**

Prem Singh
📘 Electronics & Telecommunication Engineering
💡 Enthusiast in Computer Vision & Automation

🪪 License

This project is licensed under the MIT License – feel free to use and modify it.
