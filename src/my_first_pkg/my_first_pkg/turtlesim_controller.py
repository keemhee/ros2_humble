#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # 속도 명령 메시지 타입(Twist)을 가져옴
from turtlesim.msg import Pose  # 거북이 위치 메시지 타입(Pose)을 가져옴
from turtlesim.srv import SetPen  # 펜 설정 서비스 타입(SetPen)을 가져옴

class TurtlesimControllerNode(Node):  # TurtlesimControllerNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("turtlesim_controller")  # 노드 이름을 'turtlesim_controller'로 설정하며 상위 클래스 초기화
        self.get_logger().info("turtlesim controller has been started.")  # 노드 시작 메시지를 로그에 출력
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)  # '/turtle1/pose' 토픽을 구독하며 Pose 메시지 수신, 큐 크기 10
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)  # '/turtle1/cmd_vel' 토픽으로 Twist 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.client_ = self.create_client(SetPen, '/turtle1/set_pen')  # '/turtle1/set_pen' 서비스를 호출할 클라이언트 생성
        self.pose_ = Pose()  # 거북이 위치를 저장할 Pose 객체 초기화
        time_period = 0.1  # 타이머 주기를 0.1초로 설정
        self.create_timer(time_period, self.controller_callback)  # 0.1초마다 controller_callback 함수를 호출하는 타이머 생성

    def send_request(self, r, g, b, width, off):  # 펜 설정 서비스를 호출하는 함수, RGB, 선 굵기, 펜 끄기 여부를 인자로 받음
        self.request_ = SetPen.Request()  # SetPen 서비스 요청 객체 생성
        self.request_.r = r  # 빨간색(R) 값 설정
        self.request_.g = g  # 초록색(G) 값 설정
        self.request_.b = b  # 파란색(B) 값 설정
        self.request_.width = width  # 선 굵기 설정
        self.request_.off = off  # 펜 끄기 여부 설정 (0: 켜짐, 1: 꺼짐)
        self.client_.call_async(self.request_)  # 비동기적으로 서비스 요청 전송

    def pose_callback(self, Pose):  # '/turtle1/pose' 토픽 메시지를 처리하는 콜백 함수
        '''
        self.pose_.x = pose.x  # x 좌표 저장 (주석 처리된 원래 코드)
        self.pose_.y = pose.y  # y 좌표 저장 (주석 처리된 원래 코드)
        '''
        self.pose_ = Pose  # 수신한 Pose 객체 전체를 저장
        #self.get_logger().info(f"x: {Pose.x},y: {Pose.y}, theta: {Pose.theta}")  # 위치 정보 로그 출력 (주석 처리됨)
        
    def controller_callback(self):  # 0.1초마다 실행되는 제어 로직 콜백 함수
        twist = Twist()  # Twist 메시지 객체 생성

        if self.pose_.x < 1.0 or self.pose_.x > 10.5 or self.pose_.y < 1.0 or self.pose_.y > 10.5:  # 거북이가 경계 근처에 있을 때
            twist.linear.x = 0.5  # 선속도를 0.5로 설정 (천천히 이동)
            twist.angular.z = 1.75  # 각속도를 1.75로 설정 (회전)
        else:  # 경계 안쪽에 있을 때
            twist.linear.x = 2.0  # 선속도를 2.0으로 설정 (직진)
            twist.angular.z = 0.0  # 각속도를 0.0으로 설정 (회전 없음)

        self.publisher_.publish(twist)  # 설정된 속도를 '/turtle1/cmd_vel' 토픽으로 발행

        if self.pose_.x < 5:  # x 좌표가 5 미만일 때
            self.send_request(0, 255, 0, 5, 0)  # 펜을 초록색(R:0, G:255, B:0), 굵기 5, 켜짐 상태로 설정
        else:  # x 좌표가 5 이상일 때
            self.send_request(255, 0, 0, 5, 0)  # 펜을 빨간색(R:255, G:0, B:0), 굵기 5, 켜짐 상태로 설정

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = TurtlesimControllerNode()  # TurtlesimControllerNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 및 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
