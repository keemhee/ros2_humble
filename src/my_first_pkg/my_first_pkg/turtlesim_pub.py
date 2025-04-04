#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # 속도 명령 메시지 타입(Twist)을 가져옴

class TurtlesimPubNode(Node):  # TurtlesimPubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("turtlesim_pub")  # 노드 이름을 'turtlesim_pub'로 설정하며 상위 클래스 초기화
        self.get_logger().info("turtlesim pub node has been started.")  # 노드 시작 메시지를 로그에 출력
        time_period = 1  # 타이머 주기를 1초로 설정
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)  # '/turtle1/cmd_vel' 토픽으로 Twist 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.create_timer(time_period, self.pub_callback)  # 1초마다 pub_callback 함수를 호출하는 타이머 생성

    def pub_callback(self):  # 1초마다 호출되는 콜백 함수
        msg = Twist()  # Twist 메시지 객체 생성 #msg can be other words. like twist=Twist() whatever
        msg.linear.x = 1.0  # 선속도를 1.0으로 설정 (숫자가 클수록 원 크기 증가) #bigger number, bigger circle
        #msg.linear.y = 0  # y 방향 선속도 (주석 처리, 기본값 0)
        #msg.linear.z = 0  # z 방향 선속도 (주석 처리, 기본값 0)
        #msg.angular.x = 0  # x 방향 각속도 (주석 처리, 기본값 0)
        #msg.angular.y = 0  # y 방향 각속도 (주석 처리, 기본값 0)
        msg.angular.z = 1.75  # 각속도를 1.75로 설정 (회전 속도)
        self.publisher_.publish(msg)  # 설정된 속도를 '/turtle1/cmd_vel' 토픽으로 발행
        self.get_logger().info(f'x: {msg.linear.x}, theta: {msg.angular.z}')  # 발행한 선속도와 각속도를 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = TurtlesimPubNode()  # TurtlesimPubNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
