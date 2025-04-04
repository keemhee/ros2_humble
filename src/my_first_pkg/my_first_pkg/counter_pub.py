#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from std_msgs.msg import Int32  # 정수형 메시지 타입(Int32)을 가져옴 #package.xml <depend>std_msgs</depend>

class MyCounterPub(Node):  # MyCounterPub라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("counter_pub")  # 노드 이름을 'counter_pub'로 설정하며 상위 클래스 초기화
        self.get_logger().info("counter_pub node has been started.")  # 노드 시작 메시지를 로그에 출력
        time_period = 1  # 타이머 주기를 1초로 설정 (정수형)
        self.publisher_ = self.create_publisher(Int32, "count_topic", 1)  # 'count_topic' 토픽으로 Int32 메시지를 발행할 퍼블리셔 생성 #(interface type, topic name, queue)
        self.create_timer(time_period, self.timer_callback)  # 1초마다 timer_callback 함수를 호출하는 타이머 생성
        self.count = 0  # 카운트 값을 저장하는 변수 초기화

    def timer_callback(self):  # 1초마다 호출되는 콜백 함수
        self.get_logger().info(f'current count: {self.count}')  # 현재 카운트 값을 로그에 출력 # for checking 
        msg = Int32()  # Int32 메시지 객체 생성
        msg.data = self.count  # 현재 카운트 값을 메시지 데이터에 설정
        self.publisher_.publish(msg)  # 카운트 값을 'count_topic' 토픽으로 발행
        self.count += 1  # 카운트 값을 1 증가

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = MyCounterPub()  # MyCounterPub 노드 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    rclpy.shutdown()  # ROS2 환경 종료 (node.destroy_node() 생략 시 자동 호출)

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
