#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴

class MyCounter(Node):  # MyCounter라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("my_counter_node")  # 노드 이름을 'my_counter_node'로 설정하며 상위 클래스 초기화
        self.get_logger().info("counting start")  # 카운팅 시작 메시지를 로그에 출력
        self.count = 0  # 카운트 값을 저장하는 변수 초기화
        self.create_timer(1, self.callback_counter)  # 1초마다 callback_counter 함수를 호출하는 타이머 생성
    
    def callback_counter(self):  # 1초마다 호출되는 콜백 함수
        self.count += 1  # 카운트 값을 1 증가
        self.get_logger().info(f'current count: {self.count}')  # 현재 카운트 값을 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = MyCounter()  # MyCounter 노드 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 타이머 이벤트 대기
    rclpy.shutdown()  # ROS2 환경 종료 (node.destroy_node() 생략 시 자동 호출)

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
