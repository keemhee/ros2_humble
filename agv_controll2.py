import cv2  # OpenCV 라이브러리 임포트
import numpy as np  # NumPy 라이브러리 임포트
import threading  # 스레딩 라이브러리 임포트
from pymycobot.myagv import MyAgv  # MyAgv 클래스 임포트
import sys  # 시스템 관련 라이브러리 임포트
import time  # 시간 관련 라이브러리 임포트
# AGV 객체 생성
agv = MyAgv("/dev/ttyAMA2", 115200)
run_flag = True  # 실행 플래그
direction = None  # 현재 방향
prev_direction = None  # 이전 방향
error = 0  # PID 에러
prev_error = 0  # 이전 PID 에러
integral = 0  # PID 적분 값
pid_output = 0  # PID 출력 값
# PID 제어 상수
Kp = 0.2  # 비례 상수
Ki = 0.01  # 적분 상수
Kd = 0.25  # 미분 상수
# 카메라 설정
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# PID 계산 함수
def calculate_pid(error, prev_error, integral, prev_output=0):
    derivative = error - prev_error  # 미분 값 계산
    output = Kp * error + Ki * integral + Kd * derivative  # PID 출력 계산
    output = max(min(int(output), 127), -127)  # 출력 값 제한
    smoothed_output = 0.7 * prev_output + 0.3 * output  # 출력 값 스무딩
    return int(smoothed_output)  # 정수로 변환하여 반환
# 회전 속도 계산 함수
def calculate_turn_speed(pid_output):
    min_turn_speed = 20  # 최소 회전 속도
    max_turn_speed = 80  # 최대 회전 속도
    scale_factor = 1.1  # 회전 속도 증폭 비율
    turn_speed = min_turn_speed + (max_turn_speed - min_turn_speed) * abs(pid_output) / 127  # 회전 속도 계산
    return int(turn_speed * scale_factor)  # 정수로 변환하여 반환
# 프레임 처리 함수
def process_frame(frame):
    global error, direction, integral, prev_error, pid_output, prev_direction
    height, width, _ = frame.shape  # 프레임 크기 가져오기
    roi_height = int(height / 6)  # ROI 높이 설정
    roi_top = height - roi_height  # ROI 상단 위치 설정
    roi = frame[roi_top:, :]  # ROI 설정
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # ROI를 HSV 색상 공간으로 변환
    # 노란색 범위 설정
    lower_yellow = np.array([20, 95, 125], dtype=np.uint8)
    upper_yellow = np.array([60, 255, 255], dtype=np.uint8)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)  # 노란색 마스크 생성
    # 파란색 범위 설정
    lower_blue = np.array([100, 150, 50], dtype=np.uint8)
    upper_blue = np.array([140, 255, 255], dtype=np.uint8)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 파란색 마스크 생성
    # 빨간색 범위 설정
    lower_red = np.array([170, 50, 50], dtype=np.uint8)
    upper_red = np.array([180, 255, 255], dtype=np.uint8)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)  # 빨간색 마스크 생성
    blue_detect = cv2.countNonZero(blue_mask) > 50  # 파란색 감지 여부
    yellow_detect = cv2.countNonZero(yellow_mask) > 20  # 노란색 감지 여부
    red_detect = cv2.countNonZero(red_mask) > 50  # 빨간색 감지 여부
    if blue_detect:
        direction = None  # 파란색 감지 시 방향 없음
    elif red_detect:
        direction = "SIDESTEP"  # 빨간색 감지 시 장애물 회피
    elif yellow_detect and prev_direction != "SIDESTEP":
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  # ROI를 그레이스케일로 변환
        _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)  # 이진화
        yellow_binary_image = cv2.bitwise_and(binary_image, binary_image, mask=yellow_mask)  # 노란색 이진화 이미지 생성
        yellow_contours, _ = cv2.findContours(yellow_binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 윤곽선 찾기
        if len(yellow_contours) >= 1:
            max_contour = max(yellow_contours, key=cv2.contourArea)  # 가장 큰 윤곽선 찾기
            M = cv2.moments(max_contour)  # 윤곽선의 모멘트 계산
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])  # 윤곽선의 중심 x 좌표 계산
                frame_center = yellow_binary_image.shape[1] // 2  # 프레임 중심 계산
                error = cx - frame_center  # 에러 계산
                pid_output = calculate_pid(error, prev_error, integral)  # PID 출력 계산
                prev_error = error  # 이전 에러 업데이트
                integral += error  # 적분 값 업데이트
                integral = max(min(integral, 100), -100)  # 적분 값 제한
                if pid_output > 5:  # 오른쪽 회전
                    if prev_direction != "RIGHT":
                        agv.stop()
                    direction = "RIGHT"
                elif pid_output < -5:  # 왼쪽 회전
                    if prev_direction != "LEFT":
                        agv.stop()
                    direction = "LEFT"
                else: 
                    if prev_direction != "FOWARD":
                        agv.stop()
                    direction = "FOWARD"
    else:
        direction = None  # 감지된 색상이 없을 경우 방향 없음
# 카메라 스레드 함수
def camera_thread(cap):
    while True:
        ret, frame = cap.read()  # 프레임 읽기
        if not ret:
            print("Camera error")
            break
        process_frame(frame)  # 프레임 처리
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키 입력 시 종료
            agv.stop()
            sys.exit()
            break
    agv.stop()  # AGV 정지
    cap.release()  # 카메라 해제
    cv2.destroyAllWindows()  # 모든 윈도우 닫기
# 모터 스레드 함수
def motor_thread():
    global run_flag, direction, prev_direction, pid_output
    no_detect_count = 0  # 감지되지 않은 횟수
    max_no_detect_count = 30  # 최대 감지되지 않은 횟수
    while True:
        if prev_direction == "SIDESTEP":  # 장애물 회피 중에는 다른 명령 무시
            continue
        base_speed = 128  # 기본 속도
        turn_speed = int(calculate_turn_speed(pid_output))  # 회전 속도 계산
        if direction == "RIGHT":  # 오른쪽 회전
            print(f"Turning RIGHT with PID output: {pid_output}")
            agv._mesg(base_speed + (turn_speed // 3), base_speed, base_speed - turn_speed)  # AGV 오른쪽 회전 명령
            prev_direction = "RIGHT"  # 이전 방향 업데이트
            no_detect_count = 0  # 감지되지 않은 횟수 초기화
        elif direction == "LEFT":  # 왼쪽 회전
            print(f"Turning LEFT with PID output: {pid_output}")
            agv._mesg(base_speed + (turn_speed // 3), base_speed, base_speed + turn_speed)  # AGV 왼쪽 회전 명령
            prev_direction = "LEFT"  # 이전 방향 업데이트
            no_detect_count = 0  # 감지되지 않은 횟수 초기화
        elif direction == "FOWARD":  # 직진
            print("Moving FORWARD")
            agv._mesg(base_speed + 10, base_speed, base_speed)  # AGV 직진 명령
            prev_direction = "FOWARD"  # 이전 방향 업데이트
            no_detect_count = 0  # 감지되지 않은 횟수 초기화
        elif direction == "SIDESTEP":  # 장애물 회피
            prev_direction = "SIDESTEP"  # 이전 방향 업데이트
            print(f"SIDESTEP Start")
            agv.go_ahead(10, timeout=0.6)  # AGV 전진
            agv.pan_right(10, timeout=2)  # AGV 오른쪽 회전
            agv.go_ahead(10, timeout=3.5)  # AGV 전진
            agv.pan_left(10, timeout=2)  # AGV 왼쪽 회전
            prev_direction = None  # 이전 방향 초기화
        else:
            if prev_direction == "LEFT":
                agv._mesg(base_speed, base_speed, base_speed + 10)  # AGV 왼쪽 회전 유지
                no_detect_count += 1  # 감지되지 않은 횟수 증가
                if no_detect_count >= max_no_detect_count:  # 최대 감지되지 않은 횟수 초과 시
                    agv.stop()  # AGV 정지
                    for i in range(max_no_detect_count):
                        agv._mesg(base_speed, base_speed, base_speed - 10)  # AGV 오른쪽 회전
                        time.sleep(0.1)
                    agv.stop()  # AGV 정지
                    no_detect_count = 0  # 감지되지 않은 횟수 초기화
                    prev_direction = None  # 이전 방향 초기화
            elif prev_direction == "RIGHT":
                agv._mesg(base_speed, base_speed, base_speed - 10)  # AGV 오른쪽 회전 유지
                no_detect_count += 1  # 감지되지 않은 횟수 증가
                if no_detect_count >= max_no_detect_count:  # 최대 감지되지 않은 횟수 초과 시
                    agv.stop()  # AGV 정지
                    for i in range(max_no_detect_count):
                        agv._mesg(base_speed, base_speed, base_speed + 10)  # AGV 왼쪽 회전
                        time.sleep(0.1)
                    agv.stop()  # AGV 정지
                    prev_direction = None  # 이전 방향 초기화
                    no_detect_count = 0  # 감지되지 않은 횟수 초기화
            elif direction is None:  # 정지
                print("AGV is stopping...")
                agv.stop()  # AGV 정지
                prev_direction = None  # 이전 방향 초기화
        time.sleep(0.1)  # 0.1초 대기
# 스레드 생성
camera_thread = threading.Thread(target=camera_thread, args=((cap,)))
motor_thread = threading.Thread(target=motor_thread)
# 스레드 시작
camera_thread.start()
motor_thread.start()
# 스레드 종료 대기
camera_thread.join()
motor_thread.join()
agv.stop()  # AGV 정지
