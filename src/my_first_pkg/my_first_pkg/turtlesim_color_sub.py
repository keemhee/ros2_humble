#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from turtlesim.msg import Color  # turtlesim의 Color 메시지 타입을 가져옴 (RGB 값 포함)

class TurtlesimColorSubNode(Node):  # TurtlesimColorSubNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("turtle_color")  # 노드 이름을 'turtle_color'로 설정하며 상위 클래스 초기화
        self.subscriber_ = self.create_subscription(Color,  # '/turtle1/color_sensor' 토픽을 구독하며 Color 메시지 수신
                                                    "/turtle1/color_sensor",
                                                    self.color_callback, 10)  # 큐 크기 10
        self.get_logger().info("turtle color node has been started.")  # 노드 시작 메시지를 로그에 출력

    def color_callback(self, color):  # '/turtle1/color_sensor' 토픽 메시지를 처리하는 콜백 함수
        self.get_logger().info(f"r: {color.r}, g: {color.g}, b: {color.b}")  # 수신한 RGB 값을 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = TurtlesimColorSubNode()  # TurtlesimColorSubNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
