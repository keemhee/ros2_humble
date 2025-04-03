#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import PointStamped, PoseStamped  # PointStamped(3D 좌표)와 PoseStamped(위치+방향) 메시지 타입을 가져옴

class MyNavGoalNode(Node):  # MyNavGoalNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("my_nav_goal")  # 노드 이름을 'my_nav_goal'로 설정하며 상위 클래스 초기화
        self.subscriber_ = self.create_subscription(PointStamped, "clicked_point", self.point_callback, 10)  # 'clicked_point' 토픽을 구독하며 PointStamped 메시지 수신, 큐 크기 10
        self.publisher_ = self.create_publisher(PoseStamped, "goal_pose", 10)  # 'goal_pose' 토픽으로 PoseStamped 메시지를 발행할 퍼블리셔 생성, 큐 크기 10
        self.get_logger().info("node has been started.")  # 노드 시작 메시지를 로그에 출력

    def point_callback(self, msg):  # 'clicked_point' 토픽 메시지를 처리하는 콜백 함수
        goal_pose1 = PoseStamped()  # PoseStamped 메시지 객체 생성
        goal_pose1.pose.position.x = msg.point.x  # 클릭한 좌표의 x 값을 목표 위치의 x로 설정
        goal_pose1.pose.position.y = msg.point.y  # 클릭한 좌표의 y 값을 목표 위치의 y로 설정
        goal_pose1.pose.position.z = msg.point.z  # 클릭한 좌표의 z 값을 목표 위치의 z로 설정
        
        self.publisher_.publish(goal_pose1)  # 설정된 목표 위치를 'goal_pose' 토픽으로 발행

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = MyNavGoalNode()  # MyNavGoalNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 및 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
