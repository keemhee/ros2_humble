#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from std_msgs.msg import String  # 문자열(String) 메시지 타입을 가져옴

class RobotStationNode(Node):  # RobotStationNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("robot_station1")  # 노드 이름을 'robot_station1'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(String, "robot_station3", 10)  # 'robot_station3' 토픽으로 String 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        period = 2  # 타이머 주기를 2초로 설정
        self.create_timer(period, self.timer_callback)  # 2초마다 timer_callback 함수를 호출하는 타이머 생성
        self.get_logger().info("robot_station has been started.")  # 노드 시작 메시지를 로그에 출력
    
    def timer_callback(self):  # 2초마다 호출되는 콜백 함수
        msg = String()  # String 메시지 객체 생성 #initiate
        msg.data = "Hi This is Kairos News Station"  # 메시지 데이터에 고정 문자열 설정
        self.publisher_.publish(msg)  # 설정된 메시지를 'robot_station3' 토픽으로 발행
        self.get_logger().info(msg.data)  # 발행한 메시지를 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = RobotStationNode()  # RobotStationNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    rclpy.shutdown()  # ROS2 환경 종료 (node.destroy_node() 생략 시 자동 호출)

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
