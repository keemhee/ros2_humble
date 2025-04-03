'''#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class IMGSubNode(Node):
    def __init__(self):
        super().__init__("img_sub")
        self.subscriber_=self.create_subscription(Image, 'img_raw', self.img_callback, 10)

        self.bridge = CvBridge()

        self.get_logger().info("sub node has been started.")

    def img_callback(self, img_data):
        frame = self.bridge.imgmsg_to_cv2(img_data, 'bgr8')
        cv2.imshow('Image', frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args = args)
    node = IMGSubNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()
    '''

#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from sensor_msgs.msg import Image  # ROS2 이미지 메시지 타입(Image)을 가져옴
import cv2  # OpenCV 모듈을 가져옴 (이미지 처리용)
import numpy as np  # NumPy 모듈을 가져옴 (배열 연산용)
from cv_bridge import CvBridge  # ROS2 이미지와 OpenCV 이미지 간 변환을 위한 CvBridge 모듈 가져옴

class IMGSubNode(Node):  # IMGSubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("img_sub")  # 노드 이름을 'img_sub'로 설정하며 상위 클래스 초기화
        self.subscriber_ = self.create_subscription(Image, 'img_raw', self.img_callback, 10)  # 'img_raw' 토픽을 구독하며 Image 메시지 수신, 큐 크기 10
        self.bridge = CvBridge()  # CvBridge 객체 생성 (ROS 이미지와 OpenCV 이미지 변환용)
        self.get_logger().info("sub node has been started.")  # 노드 시작 메시지를 로그에 출력

    def img_callback(self, img_data):  # 'img_raw' 토픽 메시지를 처리하는 콜백 함수
        frame = self.bridge.imgmsg_to_cv2(img_data, 'bgr8')  # ROS Image 메시지를 OpenCV BGR 형식으로 변환
        
        # Convert BGR to HSV  # BGR 이미지를 HSV 색상 공간으로 변환 (색상 감지 용이)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 프레임을 BGR에서 HSV로 변환
        
        # Define range of red color in HSV  # HSV에서 빨간색 범위를 정의
        lower_red = np.array([0, 100, 100])  # 빨간색의 하한 값 설정 (Hue: 0, Saturation: 100, Value: 100)
        upper_red = np.array([10, 255, 255])  # 빨간색의 상한 값 설정 (Hue: 10, Saturation: 255, Value: 255)
        
        # Create a mask for red color  # 빨간색에 대한 마스크 생성
        mask = cv2.inRange(hsv, lower_red, upper_red)  # HSV 이미지에서 빨간색 범위에 해당하는 마스크 생성
        
        # Bitwise-AND mask and original image  # 마스크와 원본 이미지를 비트 연산으로 결합
        red_only = cv2.bitwise_and(frame, frame, mask=mask)  # 원본 이미지에서 빨간색 부분만 추출
        
        # Display the resulting frame  # 결과 프레임을 화면에 표시
        cv2.imshow('Red Detection', red_only)  # 'Red Detection' 창에 빨간색만 표시된 이미지 출력
        cv2.waitKey(1)  # 1ms 동안 키 입력 대기 (창 업데이트용)

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = IMGSubNode()  # IMGSubNode 객체 생성
    try:  # 노드 실행 시도
        rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    except KeyboardInterrupt:  # Ctrl+C로 종료 시 예외 처리
        node.destroy_node()  # 노드 종료 및 리소스 정리
        rclpy.shutdown()  # ROS2 환경 종료

if __name__ == "__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
