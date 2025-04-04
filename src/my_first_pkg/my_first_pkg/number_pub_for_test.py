#!/usr/bin/env python3  # 스크립트를 실행할 때 사용할 Python 인터프리터를 지정
import random  # 난수 생성을 위한 random 모듈 가져오기
import rclpy  # ROS 2 Python 클라이언트 라이브러리 가져오기
from rclpy.node import Node  # ROS 2 노드 클래스 가져오기
from my_interfaces.msg import NumForTest  # 사용자 정의 메시지 타입 가져오기

class TestPubNode(Node):  # ROS 2 노드를 상속받는 TestPubNode 클래스 정의
    def __init__(self):  # 클래스 초기화 메서드
        super().__init__("test_pub")  # 부모 클래스 초기화 및 노드 이름을 "test_pub"으로 설정
        self.publisher_ = self.create_publisher(NumForTest, "random_number", 10)  # "random_number" 토픽에 대한 발행자 생성, 큐 크기는 10으로 설정
        self.create_timer(1, self.timer_callback)  # 1초마다 timer_callback 함수를 호출하는 타이머 생성
        self.get_logger().info("pub node has been started.")  # 노드가 시작되었다는 로그 메시지 출력

    def timer_callback(self):  # 타이머에 의해 주기적으로 호출되는 콜백 함수
        num = random.randint(1, 100)  # 1부터 100 사이의 난수 생성
        msg = NumForTest()  # NumForTest 메시지 객체 생성
        msg.random_number = num  # 메시지 객체에 생성된 난수 할당
        self.publisher_.publish(msg)  # 메시지를 토픽으로 발행
        self.get_logger().info(f'number: {msg.random_number}')  # 발행된 난수를 로그로 출력

def main(args=None):  # 메인 함수 정의
    rclpy.init(args = args)  # ROS 2 시스템 초기화
    node = TestPubNode()  # TestPubNode 클래스의 인스턴스 생성
    rclpy.spin(node)  # 노드가 종료될 때까지 콜백 함수 처리를 위해 대기
    node.destroy_node()  # 노드 종료
    rclpy.shutdown()  # ROS 2 시스템 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 아래 코드 실행
    main()  # 메인 함수 호출
