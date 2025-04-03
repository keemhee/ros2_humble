#!/usr/bin/env python3
# 이 스크립트는 Python 3 인터프리터로 실행됩니다.

import rclpy  # rclpy 모듈을 임포트합니다 (ROS 2 Python 클라이언트 라이브러리).
from rclpy.node import Node  # Node 클래스를 임포트합니다 (ROS 2 노드를 생성하기 위해 필요).
from my_interfaces.srv import AddThreeInts  # AddThreeInts 서비스 메시지를 임포트합니다 (사용자 정의 서비스 메시지).

class AddThreeIntsClientNode(Node):  # AddThreeIntsClientNode 클래스를 정의합니다 (Node 클래스를 상속).
    def __init__(self):  # 클래스의 생성자입니다.
        super().__init__("add_three_ints_client")  # Node 클래스의 생성자를 호출하고, 노드 이름을 "add_three_ints_client"로 설정합니다.
        self.client_ = self.create_client(AddThreeInts, 'add_three_ints')  # AddThreeInts 타입의 클라이언트를 생성하고, 서비스 이름을 'add_three_ints'로 설정합니다.
        while not self.client_.wait_for_service(timeout_sec=1):  # 서비스 서버가 준비될 때까지 대기합니다 (1초마다 확인).
            self.get_logger().info('Waiting for server')  # 서버를 기다리고 있음을 로그로 출력합니다.

        self.get_logger().info("client has been started.")  # 클라이언트가 시작되었음을 로그로 출력합니다.
        self.call_add_two_ints_service(1, 2, 3)  # call_add_two_ints_service 메서드를 호출하여 1, 2, 3의 합을 요청합니다.

    def call_add_two_ints_service(self, a, b, c):  # AddThreeInts 서비스를 호출하는 메서드입니다.
        request = AddThreeInts.Request()  # AddThreeInts 서비스 요청 객체를 생성합니다.
        request.a = a  # 요청 객체의 a 필드에 값을 할당합니다.
        request.b = b  # 요청 객체의 b 필드에 값을 할당합니다.
        request.c = c  # 요청 객체의 c 필드에 값을 할당합니다.
        future = self.client_.call_async(request)  # 비동기 서비스 호출을 수행하고, future 객체를 반환받습니다.
        future.add_done_callback(self.response_callback)  # 서비스 호출 완료 시 실행될 콜백 함수를 등록합니다.

    def response_callback(self, future):  # 서비스 응답을 처리하는 콜백 함수입니다.
        try:
            response = future.result()  # 서비스 응답 결과를 얻습니다.
            self.get_logger().info(f'Result: {response.sum}')  # 응답 결과 (합계)를 로그로 출력합니다.
        except Exception as e:  # 예외가 발생했을 경우 예외를 처리합니다.
            self.get_logger().warn(f'{e}')  # 예외 메시지를 경고 로그로 출력합니다.

def main(args=None):  # 메인 함수입니다.
    rclpy.init(args=args)  # rclpy를 초기화합니다.
    node = AddThreeIntsClientNode()  # AddThreeIntsClientNode 객체를 생성합니다.
    rclpy.spin(node)  # 노드를 실행하고, 이벤트 처리를 시작합니다.
    node.destroy_node()  # 노드를 종료하고, 자원을 해제합니다.
    rclpy.shutdown()  # rclpy를 종료합니다.

if __name__ == "__main__":  # 이 스크립트가 직접 실행되었을 때만 main 함수를 호출합니다.
    main()  # main 함수를 호출합니다.
