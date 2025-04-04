#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from turtlesim.msg import Pose  # turtlesim의 Pose 메시지 타입을 가져옴 (위치 및 속도 정보 포함)

class TurtlesimPoseSubNode(Node):  # TurtlesimPoseSubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("turtle_pose")  # 노드 이름을 'turtle_pose'로 설정하며 상위 클래스 초기화
        self.subscriber_ = self.create_subscription(Pose,  # '/turtle1/pose' 토픽을 구독하며 Pose 메시지 수신
                                                    "/turtle1/pose",
                                                    self.pose_callback, 10)  # 큐 크기 10
        self.get_logger().info("turtle pose node has been started.")  # 노드 시작 메시지를 로그에 출력

    '''
    def pose_callback(self, msg):  # 콜백 함수의 첫 번째 버전 (주석 처리됨)
        self.get_logger().info(f"x: {msg.x},y: {msg.y}, theta: {msg.theta},  # x, y 좌표와 방향(theta) 출력
                               linear velocity: {msg.linear_velocity},  # 선속도 출력
                               angular velocity: {msg.angular_velocity}")  # 각속도 출력
                               '''
    def pose_callback(self, pose):  # '/turtle1/pose' 토픽 메시지를 처리하는 콜백 함수. 거북이 이동 시 로그에 실시간 위치 및 속도 출력
        #pass  # 현재 아무 동작도 수행하지 않음 (비활성화 상태)
        #self.get_logger().info(f"x: {pose.x},y: {pose.y}, theta: {pose.theta},  # x, y 좌표와 방향(theta) 출력 (주석 처리됨)
        #                       linear velocity: {pose.linear_velocity},  # 선속도 출력 (주석 처리됨)
        #                       angular velocity: {pose.angular_velocity}")  # 각속도 출력 (주석 처리됨)
        self.get_logger().info(f"x: {pose.x}, y: {pose.y}, theta: {pose.theta}, linear velocity: {pose.linear_velocity}, angular velocity: {pose.angular_velocity}")


def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = TurtlesimPoseSubNode()  # TurtlesimPoseSubNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
