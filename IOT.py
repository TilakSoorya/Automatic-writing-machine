import cv2
import time
import pyautogui
import serial
# ser = serial.Serial('COM3', 9600)
# ser.open()

import serial
import time
arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(x.encode())
    time.sleep(0.05)
    data = arduino.readline()
    return data

def find_green_dot_position(image):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = (40, 50, 50)
    upper_green = (80, 255, 255)
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest_contour)
        cx = int(moments['m10'] / moments['m00'])
        image_width = image.shape[1]
        if cx < image_width // 2:
            return "Left"
        else:
            return "Right"
    else:
        return "No green dot found"



delay = 10
while True:
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot_{}.png'.format(timestamp))
    image_path = 'screenshot_{}.png'.format(timestamp)
    dot_position = find_green_dot_position(screenshot)
    # ser.write(dot_position.encode())
    pos = write_read(dot_position)
    print("Green dot position:",pos)

    time.sleep(delay)

