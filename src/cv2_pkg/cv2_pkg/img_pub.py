#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from sensor_msgs.msg import Image  # ROS2 이미지 메시지 타입(Image)을 가져옴
import cv2  # OpenCV 모듈을 가져옴 (카메라 캡처 및 이미지 처리용)
from cv_bridge import CvBridge  # ROS2 이미지와 OpenCV 이미지 간 변환을 위한 CvBridge 모듈 가져옴

class IMGPubNode(Node):  # IMGPubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("img_pub")  # 노드 이름을 'img_pub'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(Image, 'img_raw', 10)  # 'img_raw' 토픽으로 Image 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.create_timer(0.1, self.img_callback)  # 0.1초마다 img_callback 함수를 호출하는 타이머 생성
        self.cap = cv2.VideoCapture(0)  # 시스템의 기본 카메라(인덱스 0)를 열기
        self.bridge = CvBridge()  # CvBridge 객체 생성 (OpenCV 이미지와 ROS 이미지 변환용)
        self.get_logger().info("pub node has been started")  # 노드 시작 메시지를 로그에 출력

    def img_callback(self):  # 이미지를 캡처하고 발행하는 콜백 함수
        ret, frame = self.cap.read()  # 카메라에서 프레임 읽기 (ret: 성공 여부, frame: 이미지 데이터)
        img_data = self.bridge.cv2_to_imgmsg(frame, 'bgr8')  # OpenCV BGR 이미지를 ROS Image 메시지로 변환 (bgr8 형식)
        self.publisher_.publish(img_data)  # 변환된 이미지 데이터를 'img_raw' 토픽으로 발행

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = IMGPubNode()  # IMGPubNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
