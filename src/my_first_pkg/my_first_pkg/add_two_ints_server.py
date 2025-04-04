#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from example_interfaces.srv import AddTwoInts  # AddTwoInts 서비스 타입을 가져옴 (두 정수를 더하는 서비스)

class AddTwoIntsServerNode(Node):  # AddTwoIntsServerNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("add_two_ints_server")  # 노드 이름을 'add_two_ints_server'로 설정하며 상위 클래스 초기화
        self.server_ = self.create_service(AddTwoInts, 'add_two_ints', self.add_callback)  # 'add_two_ints' 서비스를 생성하고 요청 처리 콜백 지정
        self.get_logger().info("server has been started.")  # 서버 시작 메시지를 로그에 출력

    def add_callback(self, request, response):  # 서비스 요청을 처리하는 콜백 함수
        '''a = request.a  # 요청에서 첫 번째 정수(a)를 변수에 저장 (주석 처리된 불필요한 코드)
        b = request.b  # 요청에서 두 번째 정수(b)를 변수에 저장 (주석 처리된 불필요한 코드)
        response.sum = a + b'''  # 합계를 계산해 응답에 저장 (주석 처리된 불필요한 코드)
        response.sum = request.a + request.b  # 요청의 두 정수를 더해 응답의 합계(sum)에 저장
        self.get_logger().info(f'{request.a} + {request.b} = {response.sum}')  # 요청 값과 결과를 로그에 출력
        return response  # 계산된 응답 객체를 클라이언트에 반환

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = AddTwoIntsServerNode()  # AddTwoIntsServerNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 서비스 요청 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
