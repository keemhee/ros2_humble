#!/usr/bin/env python3
# 이 스크립트는 Python 3 인터프리터로 실행됩니다.

import rclpy  # rclpy 모듈을 임포트합니다 (ROS 2 Python 클라이언트 라이브러리).
from rclpy.node import Node  # Node 클래스를 임포트합니다 (ROS 2 노드를 생성하기 위해 필요).
from my_interfaces.srv import AddThreeInts  # AddThreeInts 서비스 메시지를 임포트합니다 (사용자 정의 서비스 메시지).

class AddThreeIntsServerNode(Node):  # AddThreeIntsServerNode 클래스를 정의합니다 (Node 클래스를 상속).
    def __init__(self):  # 클래스의 생성자입니다.
        super().__init__("add_three_ints_server")  # Node 클래스의 생성자를 호출하고, 노드 이름을 "add_three_ints_server"로 설정합니다.
        self.server_ = self.create_service(AddThreeInts, 'add_three_ints', self.add_callback)  # AddThreeInts 타입의 서비스를 생성하고, 서비스 이름을 'add_three_ints'로 설정하며, 콜백 함수를 등록합니다.
        self.get_logger().info("server has been started.")  # 서버가 시작되었음을 로그로 출력합니다.

    def add_callback(self, request, response):  # 서비스 요청을 처리하는 콜백 함수입니다.
        response.sum = request.a + request.b + request.c  # 요청에서 받은 세 정수를 더하여 응답 객체의 sum 필드에 할당합니다.
        self.get_logger().info(f'{request.a} + {request.b} + {request.c} = {response.sum}')  # 요청받은 값들과 그 합계를 로그로 출력합니다.
        return response  # 응답 객체를 반환합니다.

def main(args=None):  # 메인 함수입니다.
    rclpy.init(args=args)  # rclpy를 초기화합니다.
    node = AddThreeIntsServerNode()  # AddThreeIntsServerNode 객체를 생성합니다.
    rclpy.spin(node)  # 노드를 실행하고, 이벤트 처리를 시작합니다.
    node.destroy_node()  # 노드를 종료하고, 자원을 해제합니다.
    rclpy.shutdown()  # rclpy를 종료합니다.

if __name__ == "__main__":  # 이 스크립트가 직접 실행되었을 때만 main 함수를 호출합니다.
    main()  # main 함수를 호출합니다.
