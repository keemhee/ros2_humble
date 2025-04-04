#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from std_msgs.msg import String, Int32  # 문자열(String)과 정수(Int32) 메시지 타입을 가져옴

class RobotStationSubNode(Node):  # RobotStationSubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("sub_news")  # 노드 이름을 'sub_news'로 설정하며 상위 클래스 초기화
        self.subscriber_ = self.create_subscription(String, "robot_station3", self.news_callback, 10)  # 'robot_station3' 토픽을 구독하며 String 메시지 수신 #interface type, topic name, callback, queue size
        self.subscriber_count = self.create_subscription(Int32, "count_topic", self.count_callback, 1)  # 'count_topic' 토픽을 구독하며 Int32 메시지 수신
        self.get_logger().info("sub_news node has been started.")  # 노드 시작 메시지를 로그에 출력

    def news_callback(self, msg):  # 'robot_station3' 토픽 메시지를 처리하는 콜백 함수
        # print in terminal  # 터미널에 출력 (주석으로 의도 표시)
        self.get_logger().info(msg.data)  # 수신한 문자열 메시지를 로그에 출력

    def count_callback(self, msg):  # 'count_topic' 토픽 메시지를 처리하는 콜백 함수
        self.get_logger().info(f"{msg.data}")  # 수신한 정수 메시지를 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = RobotStationSubNode()  # RobotStationSubNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
