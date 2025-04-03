#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
import sys  # 명령줄 인자를 처리하기 위한 모듈 가져옴
from geometry_msgs.msg import Twist  # 속도 명령 메시지 타입(Twist)을 가져옴

class AngularVelocityNode(Node):  # AngularVelocityNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("angular_velocity_node")  # 노드 이름을 'angular_velocity_node'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)  # '/turtle1/cmd_vel' 토픽으로 Twist 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.create_timer(0.1, self.angular_callback)  # 0.1초마다 angular_callback 함수를 호출하는 타이머 생성
        self.get_logger().info("Node has been started.")  # 노드 시작 메시지를 로그에 출력

    def angular_callback(self):  # 각속도를 계산하고 발행하는 콜백 함수
        try:  # 명령줄 인자 처리 중 오류를 잡기 위한 try 블록 시작
            msg = Twist()  # Twist 메시지 객체 생성
            # w = v/r  # 각속도 공식: w(angular velocity) = v(linear velocity) / r(radius)
            msg.linear.x = float(sys.argv[1])  # 명령줄 첫 번째 인자를 선속도(linear.x)로 설정
                                               #radius = float(sys.argv[2])  # 반경을 변수로 저장 (실제 사용은 없음)
            msg.angular.z = msg.linear.x / float(sys.argv[2])  # 각속도(angular.z)를 선속도/반경으로 계산
            self.publisher_.publish(msg)  # 계산된 속도 명령을 '/turtle1/cmd_vel' 토픽으로 발행
        except (IndexError, ValueError) as e:  # 인자 부족(IndexError) 또는 숫자 변환 실패(ValueError) 예외 처리
            self.get_logger().error(f"Invalid arguments: {e}. Usage: <velocity> <radius>")  # 오류 메시지와 사용법 출력
            rclpy.shutdown()  # 오류 발생 시 ROS2 환경 종료

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = AngularVelocityNode()  # AngularVelocityNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
