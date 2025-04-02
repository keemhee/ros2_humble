from pymycobot.mycobot import MyCobot  # MyCobot 로봇 팔 제어 라이브러리 가져오기
import time  # 시간 지연을 위한 모듈 가져오기
import cv2  # OpenCV 모듈 가져오기 (이미지 처리용)
import os  # 파일 및 디렉토리 작업을 위한 모듈 가져오기
import shutil  # 파일 압축 및 복사를 위한 모듈 가져오기
import numpy as np  # 배열 연산을 위한 NumPy 모듈 가져오기
import threading  # 멀티스레딩을 위한 모듈 가져오기

servo_speed = 30  # 로봇 팔 서보 모터의 이동 속도 설정 (단위: 도/초)
servo_point = [[(-76.24),(-50),(-45),15.73,95.53,19.42],[-71.63, -25.83, -89.2, 23.55, 92.19, 21.18]]  # 로봇 팔의 기본 위치 좌표 (초기/중간 위치)
servo_color_point = [[2.63,(-63.1),(-10),15.46,90.79,5], [-133, 10, -76, -2, 94, 19],[-20, -50, -10, -20, 90, 0]]  # 색상별 목표 위치 좌표 (파랑, 초록, 주황)

is_move = False  # 로봇 팔 이동 상태를 나타내는 플래그 (현재 사용되지 않음)

def servo_move(result_servo_point):  # 로봇 팔을 제어하는 함수, 색상 인덱스를 인자로 받음
    mc.send_angles([0,0,0,0,0,0],servo_speed)  # 로봇 팔을 초기 위치(모두 0도)로 이동
    time.sleep(4)  # 4초 대기 (이동 완료까지)
    mc.send_angles(servo_point[1],servo_speed)  # 물체를 집기 위한 중간 위치로 이동
    time.sleep(4)  # 4초 대기
    mc.set_eletric_gripper(1)  # 전동 그리퍼를 활성화 (닫기 준비)
    mc.set_gripper_value(0,20)  # 그리퍼를 닫아서 물체를 집음 (값 0: 완전 닫힘, 속도 20)
    time.sleep(2)  # 2초 대기
    mc.send_angles([0,0,0,0,0,0],servo_speed)  # 다시 초기 위치로 이동
    time.sleep(5)  # 5초 대기
    mc.send_angles(servo_color_point[result_servo_point],servo_speed)  # 감지된 색상에 맞는 목표 위치로 이동
    time.sleep(4)  # 4초 대기
    mc.set_eletric_gripper(0)  # 그리퍼를 비활성화 (열기 준비)
    mc.set_gripper_value(100,20)  # 그리퍼를 열어서 물체를 놓음 (값 100: 완전 열림, 속도 20)
    time.sleep(2)  # 2초 대기
    mc.send_angles([0,0,0,0,0,0],servo_speed)  # 초기 위치로 복귀
    time.sleep(4)  # 4초 대기
    mc.send_angles(servo_point[0],servo_speed)  # 시작 위치로 돌아감
    time.sleep(4)  # 4초 대기

def detect_color(frame):  # 카메라 프레임에서 색상을 감지하는 함수
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 프레임을 BGR에서 HSV 색상 공간으로 변환

    #Blue
    lower_blue = np.array([100, 150, 50])  # 파란색의 HSV 하한 값 설정
    upper_blue = np.array([140, 255, 255])  # 파란색의 HSV 상한 값 설정
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)  # 파란색 영역 마스크 생성

    #Green
    lower_green = np.array([60, 200, 60])  # 초록색의 HSV 하한 값 설정
    upper_green = np.array([90, 230, 90])  # 초록색의 HSV 상한 값 설정
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)  # 초록색 영역 마스크 생성

    #Orange
    lower_orange = np.array([5, 150, 50])  # 주황색의 HSV 하한 값 설정
    upper_orange = np.array([30, 255, 255])  # 주황색의 HSV 상한 값 설정
    orange_mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)  # 주황색 영역 마스크 생성

    blue_detect = cv2.countNonZero(blue_mask) > 20  # 파란색 픽셀이 20개 이상이면 감지
    print(blue_detect)  # 파란색 감지 여부 출력
    green_detect = cv2.countNonZero(green_mask) > 20  # 초록색 픽셀이 20개 이상이면 감지
    print(green_detect)  # 초록색 감지 여부 출력
    orange_detect = cv2.countNonZero(orange_mask) > 20  # 주황색 픽셀이 20개 이상이면 감지
    print(orange_detect)  # 주황색 감지 여부 출력

    if blue_detect:  # 파란색이 감지되면
        print("blue detect")  # "파란색 감지" 출력
        return 0  # 파란색 인덱스(0) 반환
    elif green_detect:  # 초록색이 감지되면
        print("green_detect")  # "초록색 감지" 출력
        return 1  # 초록색 인덱스(1) 반환
    elif orange_detect:  # 주황색이 감지되면
        print("orange_detect")  # "주황색 감지" 출력
        return 2  # 주황색 인덱스(2) 반환

    return -1  # 색상이 감지되지 않으면 -1 반환

dir = 'images'  # 이미지를 저장할 디렉토리 이름 설정
os.makedirs(dir, exist_ok=True)  # 'images' 디렉토리 생성 (이미 있으면 무시)
count = 0  # 저장된 이미지 파일의 카운트 변수 초기화
zip_dir = 'img_zip'  # 압축 파일을 저장할 디렉토리 이름 설정
os.makedirs(zip_dir, exist_ok=True)  # 'img_zip' 디렉토리 생성 (이미 있으면 무시)

mc = MyCobot('COM6', 115200)  # MyCobot 객체 생성 (COM6 포트, 115200 보드레이트)
time.sleep(1)  # 1초 대기 (로봇 초기화 안정화)
mc.set_gripper_calibration()  # 그리퍼 캘리브레이션 설정
mc.set_gripper_mode(0)  # 그리퍼 모드를 0으로 설정 (기본 모드)
mc.init_eletric_gripper()  # 전동 그리퍼 초기화
time.sleep(1)  # 1초 대기

mc.send_angles([0,0,0,0,0,0],servo_speed)  # 로봇 팔을 초기 위치(모두 0도)로 이동
time.sleep(5)  # 5초 대기
mc.send_angles(servo_point[0],servo_speed)  # 시작 위치로 이동
time.sleep(5)  # 5초 대기

cap = cv2.VideoCapture(1)  # 카메라(인덱스 1) 열기

while True:  # 무한 루프 시작
    _, frame = cap.read()  # 카메라에서 프레임 읽기
    frame = cv2.flip(frame, 0)  # 프레임을 수직으로 뒤집기 (0: 상하 반전)
    key = cv2.waitKey(1) & 0xff  # 키 입력 대기 (1ms, 0xff로 8비트 값만 추출)

    if key == ord('q'):  # 'q' 키를 누르면
        break  # 루프 종료
    if key == ord('s'):  # 's' 키를 누르면
        path = os.path.join(dir, f'img_{count}.jpg')  # 저장할 이미지 경로 생성 (예: images/img_0.jpg)
        cv2.imwrite(path , frame)  # 현재 프레임을 이미지 파일로 저장
        print("Image captured")  # "이미지 캡처됨" 출력
        count += 1  # 이미지 카운트 증가 (다음 파일명에 반영)

        result_servo_point = detect_color(frame)  # 프레임에서 색상 감지
        if result_servo_point > -1:  # 유효한 색상이 감지되면
            thread = threading.Thread(target=servo_move, args=(result_servo_point,))  # 로봇 팔 이동을 스레드로 실행
            thread.start()  # 스레드 시작 (카메라와 로봇 동작 병렬 처리)
        
    cv2.imshow("Detection", frame)  # "Detection" 창에 프레임 표시

cap.release()  # 카메라 리소스 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기

zip_dir_path = os.path.join(zip_dir, 'archive')  # 압축 파일 경로 설정 (img_zip/archive)
shutil.make_archive(zip_dir_path , 'zip', dir)  # 'images' 디렉토리를 zip 파일로 압축 (archive.zip 생성)
