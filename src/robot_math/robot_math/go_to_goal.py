#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # 속도 명령 메시지 타입(Twist)을 가져옴
from turtlesim.msg import Pose  # 거북이의 위치와 방향 메시지 타입(Pose)을 가져옴
import sys  # 명령줄 인자를 처리하기 위한 모듈 가져옴
import math  # 수학 연산(거리, 각도 계산)을 위한 모듈 가져옴

class GoToGoalNode(Node):  # GoToGoalNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("go_to_goal_node")  # 노드 이름을 'go_to_goal_node'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)  # '/turtle1/cmd_vel' 토픽으로 Twist 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)  # '/turtle1/pose' 토픽을 구독하며 Pose 메시지 수신, 큐 크기 10
        self.create_timer(0.1, self.go_to_goal)  # 0.1초마다 go_to_goal 함수를 호출하는 타이머 생성
        self.get_logger().info("Node has been started.")  # 노드 시작 메시지를 로그에 출력

    def pose_callback(self, data):  # '/turtle1/pose' 토픽 메시지를 처리하는 콜백 함수
        self.pose = data  # 수신한 거북이의 현재 위치와 방향을 클래스 변수에 저장

    def go_to_goal(self):  # 목표로 이동하는 제어 로직을 실행하는 함수
        goal = Pose()  # 목표 위치와 방향을 저장할 Pose 객체 생성
        goal.x = float(sys.argv[1])  # 명령줄 첫 번째 인자를 목표 x 좌표로 설정
        goal.y = float(sys.argv[2])  # 명령줄 두 번째 인자를 목표 y 좌표로 설정
        goal.theta = float(sys.argv[3])  # 명령줄 세 번째 인자를 목표 방향(theta)으로 설정
        distance_tolerance = 0.1  # 목표에 도달했다고 판단하는 거리 허용 오차 설정 (0.1 단위)
        angle_tolerance = 0.01  # 목표 방향에 도달했다고 판단하는 각도 허용 오차 설정 (0.01 라디안)

        distance_to_goal = math.sqrt((goal.x - self.pose.x)**2 + (goal.y - self.pose.y)**2)  # 현재 위치와 목표 간 유클리드 거리 계산
        angle_to_goal = math.atan2(goal.y - self.pose.y, goal.x - self.pose.x) - self.pose.theta  # 목표 방향과 현재 방향 간 각도 차이 계산

        self.get_logger().info(f"Remaining Distance: {distance_to_goal:.3f}, Remaining Angle: {angle_to_goal:.3f}")  # 남은 거리와 각도를 로그로 출력

        new_vel = Twist()  # 속도 명령을 저장할 Twist 객체 생성
        if abs(angle_to_goal) > angle_tolerance:  # 목표 방향과의 각도 차이가 허용 오차보다 크면
            new_vel.angular.z = 5 * angle_to_goal  # 각속도를 설정해 회전 (비례 제어, 게인 5)
        elif distance_to_goal > distance_tolerance:  # 각도가 맞고 거리가 허용 오차보다 크면
            new_vel.linear.x = 5 * distance_to_goal  # 선속도를 설정해 직진 (비례 제어, 게인 5)
        else:  # 거리와 각도가 모두 허용 오차 내에 있으면
            self.get_logger().info("Goal Reached")  # 목표 도달 메시지 출력
            quit()  # 프로그램 종료

        self.publisher_.publish(new_vel)  # 계산된 속도 명령을 '/turtle1/cmd_vel' 토픽으로 발행

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = GoToGoalNode()  # GoToGoalNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 및 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리 (정상 종료 시 실행 안 됨)

if __name__ == "__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
