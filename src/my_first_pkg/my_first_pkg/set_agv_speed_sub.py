#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
#from my_interfaces.srv import Move  # 사용자 정의 Move 서비스 타입을 가져옴 (이 코드에서는 사용되지 않음)
from geometry_msgs.msg import Twist  # 속도 명령 메시지 타입(Twist)을 가져옴

class SetAgvSpeedSubNode(Node):  # SetAgvSpeedSubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("set_agv_speed_sub")  # 노드 이름을 'set_agv_speed_sub'로 설정하며 상위 클래스 초기화
        self.subscriber_ = self.create_subscription(Twist, "cmd_vel", self.agv_callback, 10)  # 'cmd_vel' 토픽을 구독하며 Twist 메시지 수신, 큐 크기 10
        self.get_logger().info("set_agv_speed sub node has been started.")  # 노드 시작 메시지를 로그에 출력

    def agv_callback(self, msg):  # 'cmd_vel' 토픽 메시지를 처리하는 콜백 함수
        self.get_logger().info(f"x = {msg.linear.x}, z = {msg.angular.z} ")  # 수신한 선속도(x)와 각속도(z)를 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = SetAgvSpeedSubNode()  # SetAgvSpeedSubNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
