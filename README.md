# Coin_detection_example
Using openCV to detect single or multiple coins from images.

# Description
This project was made for detecting coins from image using OpenCV function HoughCircles() and masking technique.

# Requirements

1. caer==2.0.8
2. mypy==0.961
3. mypy-extensions==0.4.3
4. numpy==1.23.0
5. opencv-contrib-python==4.6.0.66
6. tomli==2.0.1
7. typing-extensions==4.2.0openCV

You can install all the required libraries by running the following command

#### pip install requirements.txt

# Functionalities

1. Read & Resize image
2. Create Blank image
3. Convert to grayscale & apply gaussian blur
4. Apply Hough transform on the blurred image
5. Draw circles and apply masking

# Procedure

1. Select the image
2. Run the coin_detection.py to detect the coins from the image.

# Input image
![coin1](https://user-images.githubusercontent.com/44630419/177001202-b35ec0db-67da-4794-b73b-06f792a54c3c.jpg)

# Result

1. Coins 

![Coins_Screenshot ](https://user-images.githubusercontent.com/44630419/177001232-a708fc94-3614-400a-ac54-f7c07bc3f2c4.jpg)

2. masked 

![masked_Screenshot](https://user-images.githubusercontent.com/44630419/177001240-5d83a4fe-1977-41bc-a86d-318a65fa3b6e.jpg)
