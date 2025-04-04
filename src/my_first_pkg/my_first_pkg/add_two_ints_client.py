#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from example_interfaces.srv import AddTwoInts  # AddTwoInts 서비스 타입을 가져옴 (두 정수를 더하는 서비스)

class AddTwoIntsClientNode(Node):  # AddTwoIntsClientNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("add_two_ints_client")  # 노드 이름을 'add_two_ints_client'로 설정하며 상위 클래스 초기화
        self.client_ = self.create_client(AddTwoInts, 'add_two_ints')  # 'add_two_ints' 서비스를 호출할 클라이언트 생성
        while not self.client_.wait_for_service(timeout_sec=1):  # 서비스 서버가 준비될 때까지 대기 (1초 타임아웃)
            self.get_logger().info('Waiting for server')  # 서버 대기 중임을 로그에 출력
        self.get_logger().info("client has been started.")  # 클라이언트 시작 메시지를 로그에 출력
        self.call_add_two_ints_service(4, 6)  # 서비스 호출 함수 실행, 두 정수 4와 6을 인자로 전달 #set a(int64), b(int64)

    def call_add_two_ints_service(self, a, b):  # 서비스를 호출하는 함수, a와 b를 인자로 받음
        request = AddTwoInts.Request()  # AddTwoInts 서비스 요청 객체 생성
        request.a = a  # 요청 객체의 첫 번째 정수(a) 설정
        request.b = b  # 요청 객체의 두 번째 정수(b) 설정
        future = self.client_.call_async(request)  # 비동기적으로 서비스 요청 전송, future 객체 반환 # future => result => response
        future.add_done_callback(self.response_callback)  # 요청 완료 시 호출할 콜백 함수 등록

    def response_callback(self, future):  # 서비스 응답을 처리하는 콜백 함수
        try:  # 응답 처리 중 예외를 잡기 위한 try 블록
            response = future.result()  # future 객체에서 서비스 응답 결과 가져오기
            self.get_logger().info(f'Result: {response.sum}')  # 응답의 합계(sum)를 로그에 출력
        except Exception as e:  # 응답 처리 중 오류 발생 시 예외 처리
            self.get_logger().warn(f'{e}')  # 오류 메시지를 경고 로그로 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = AddTwoIntsClientNode()  # AddTwoIntsClientNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 서비스 요청 및 응답 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
