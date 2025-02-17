from pymycobot.mycobot import MyCobot
import time
import cv2 
import os
import shutil
import numpy as np
import threading

servo_speed = 30
servo_point = [[(-76.24),(-50),(-45),15.73,95.53,19.42],[-71.63, -25.83, -89.2, 23.55, 92.19, 21.18]]
servo_color_point = [[2.63,(-63.1),(-10),15.46,90.79,5], [-133, 10, -76, -2, 94, 19],[-20, -50, -10, -20, 90, 0]]

is_move = False

def servo_move(result_servo_point):
    mc.send_angles([0,0,0,0,0,0],servo_speed)
    time.sleep(4)
    mc.send_angles(servo_point[1],servo_speed)
    time.sleep(4)
    mc.set_eletric_gripper(1)
    mc.set_gripper_value(0,20)
    time.sleep(2)
    mc.send_angles([0,0,0,0,0,0],servo_speed)
    time.sleep(5) 
    mc.send_angles(servo_color_point[result_servo_point],servo_speed)
    time.sleep(4)
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(100,20)
    time.sleep(2)
    mc.send_angles([0,0,0,0,0,0],servo_speed)
    time.sleep(4)
    mc.send_angles(servo_point[0],servo_speed)
    time.sleep(4)

def detect_color(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Blue
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    #Green
    lower_green = np.array([60, 200, 60])
    upper_green = np.array([90, 230, 90])
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    #Orange
    lower_orange = np.array([5, 150, 50])
    upper_orange = np.array([30, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)

    blue_detect = cv2.countNonZero(blue_mask) > 20
    print(blue_detect)
    green_detect = cv2.countNonZero(green_mask) > 20
    print(green_detect)
    orange_detect = cv2.countNonZero(orange_mask) > 20
    print(orange_detect)

    if blue_detect:
        print("blue detect")
        return 0
    elif green_detect:
        print("green_detect")
        return 1
    elif orange_detect:
        print("orange_detect")
        return 2

    return -1

dir = 'images'
os.makedirs(dir, exist_ok=True)
count = 0
zip_dir = 'img_zip'
os.makedirs(zip_dir, exist_ok= True)


mc = MyCobot('COM6', 115200)
time.sleep(1)
mc.set_gripper_calibration()
mc.set_gripper_mode(0)
mc.init_eletric_gripper()
time.sleep(1)

mc.send_angles([0,0,0,0,0,0],servo_speed)
time.sleep(5)
mc.send_angles(servo_point[0],servo_speed)
time.sleep(5)

# os.path.join(dir, f'image_{count}.jpg')
cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 0)
    key = cv2.waitKey(1) & 0xff  

    if key == ord('q'):
        break
    if key == ord('s'):
        path = os.path.join(dir, f'img_{count}.jpg') 
        cv2.imwrite(path , frame)
        print("Image captured")

        result_servo_point = detect_color(frame)
        if result_servo_point > -1:
            thread = threading.Thread(target=servo_move, args=(result_servo_point,))
            thread.start()
        
    cv2.imshow("Detection", frame)

cap.release()
cv2.destroyAllWindows()

zip_dir_path = os.path.join(zip_dir, 'archive')
shutil.make_archive(zip_dir_path , 'zip', dir)
