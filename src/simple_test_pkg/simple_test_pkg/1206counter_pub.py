#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from std_msgs.msg import Int32  # 정수형 메시지 타입(Int32)을 가져옴

class CounterPubTest(Node):  # CounterPubTest라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("counter_pub")  # 노드 이름을 'counter_pub'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(Int32, "counter_pub", 1)  # 'counter_pub' 토픽으로 Int32 메시지를 발행할 퍼블리셔 생성, 큐 크기 1
        self.create_timer(1, self.counter_callback)  # 1초마다 counter_callback 함수를 호출하는 타이머 생성
        self.get_logger().info("test started")  # 노드 시작 메시지를 로그에 출력
        self.count = 0  # 카운트 값을 저장하는 변수 초기화

    def counter_callback(self):  # 1초마다 호출되는 콜백 함수
        count = Int32()  # Int32 메시지 객체 생성
        count.data = self.count  # 현재 카운트 값을 메시지 데이터에 설정
        self.publisher_.publish(count)  # 카운트 값을 'counter_pub' 토픽으로 발행
        self.count += 1  # 카운트 값을 1 증가
        self.get_logger().info(f'current count: {count.data}')  # 현재 카운트 값을 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = CounterPubTest()  # CounterPubTest 노드 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
