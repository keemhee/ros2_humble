#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # 속도 명령 메시지 타입(Twist)을 가져옴
from my_interfaces.srv import Move  # 사용자 정의 Move 서비스 타입을 가져옴

class AgvSpeedControllerNode(Node):  # AgvSpeedControllerNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("set_agv_speed")  # 노드 이름을 'set_agv_speed'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)  # 'cmd_vel' 토픽으로 Twist 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.server_ = self.create_service(Move, 'set_agv_speed', self.speed_callback)  # 'set_agv_speed' 서비스를 생성하고 요청 처리 콜백 지정
        self.twist = Twist()  # Twist 메시지 객체 생성 (속도 저장용)
        self.twist.linear.x = 3.0  # 초기 선속도를 3.0으로 설정
        self.twist.angular.z = 1.5  # 초기 각속도를 1.5로 설정
        self.create_timer(1, self.controller_callback)  # 1초마다 controller_callback 함수를 호출하는 타이머 생성
        self.get_logger().info("agv speed controller has been started. linear velocity = 3.0, angular velocity = 1.5")  # 노드 시작 및 초기 속도 메시지를 로그에 출력

    def controller_callback(self):  # 1초마다 속도를 발행하는 콜백 함수
        self.publisher_.publish(self.twist)  # 현재 Twist 객체를 'cmd_vel' 토픽으로 발행

    def speed_callback(self, request, response):  # 서비스 요청을 처리하는 콜백 함수
        self.twist.linear.x = request.linear_velocity  # 요청에서 받은 선속도로 업데이트
        self.twist.angular.z = request.angular_velocity  # 요청에서 받은 각속도로 업데이트
        response.success = True  # 응답의 성공 여부를 True로 설정
        response.message = 'speed changed.'  # 응답 메시지를 'speed changed.'로 설정
        self.get_logger().info(f'new linear velocity = {self.twist.linear.x}, new angular velocity = {self.twist.angular.z}')  # 새로운 속도 값을 로그에 출력
        return response  # 설정된 응답 객체를 클라이언트에 반환

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = AgvSpeedControllerNode()  # AgvSpeedControllerNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 서비스 요청과 토픽 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
