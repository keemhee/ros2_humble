#!/usr/bin/env python3  # 스크립트를 실행할 때 사용할 Python 인터프리터를 지정
import rclpy  # ROS 2 Python 클라이언트 라이브러리 가져오기
from rclpy.node import Node  # ROS 2 노드 클래스 가져오기
from my_interfaces.msg import NumForTest  # 사용자 정의 메시지 타입 가져오기

class TestSubNode(Node):  # ROS 2 노드를 상속받는 TestSubNode 클래스 정의
    def __init__(self):  # 클래스 초기화 메서드
        super().__init__("test_sub")  # 부모 클래스 초기화 및 노드 이름을 "test_sub"으로 설정
        self.subscriber_ = self.create_subscription(NumForTest, "random_number", self.num_callback, 10)  # "random_number" 토픽을 구독하고 메시지 수신 시 num_callback 호출, 큐 크기는 10
        self.get_logger().info("sub node has been started.")  # 노드가 시작되었다는 로그 메시지 출력
        
    def num_callback(self, msg):  # 메시지 수신 시 호출되는 콜백 함수
        self.get_logger().info(f"{msg.random_number}")  # 수신한 메시지의 random_number 값을 로그로 출력
        
def main(args=None):  # 메인 함수 정의
    rclpy.init(args = args)  # ROS 2 시스템 초기화
    node = TestSubNode()  # TestSubNode 클래스의 인스턴스 생성
    rclpy.spin(node)  # 노드가 종료될 때까지 콜백 함수 처리를 위해 대기
    node.destroy_node()  # 노드 종료
    rclpy.shutdown()  # ROS 2 시스템 종료
    
if __name__=="__main__":  # 스크립트가 직접 실행될 때만 아래 코드 실행
    main()  # 메인 함수 호출
