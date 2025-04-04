#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from my_interfaces.srv import Move  # 사용자 정의 Move 서비스 타입을 가져옴

class AgvSpeedClientNode(Node):  # AgvSpeedClientNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("set_agv_speed_client")  # 노드 이름을 'set_agv_speed_client'로 설정하며 상위 클래스 초기화
        self.client_ = self.create_client(Move, 'set_agv_speed')  # 'set_agv_speed' 서비스를 호출할 클라이언트 생성
        while not self.client_.wait_for_service(timeout_sec=1):  # 서비스 서버가 준비될 때까지 대기 (1초 타임아웃)
            self.get_logger().info('Waiting for server')  # 서버 대기 중임을 로그에 출력
        self.get_logger().info("client has been started.")  # 클라이언트 시작 메시지를 로그에 출력
        self.call_service(1.0, 2.0)  # 서비스 호출 함수 실행, 선속도 1.0과 각속도 2.0을 인자로 전달

    def call_service(self, x, z):  # 서비스를 호출하는 함수, 선속도(x)와 각속도(z)를 인자로 받음
        request = Move.Request()  # Move 서비스 요청 객체 생성
        request.linear_velocity = x  # 요청 객체에 선속도 설정
        request.angular_velocity = z  # 요청 객체에 각속도 설정
        future = self.client_.call_async(request)  # 비동기적으로 서비스 요청 전송, future 객체 반환
        future.add_done_callback(self.response_callback)  # 요청 완료 시 호출할 콜백 함수 등록

    def response_callback(self, future):  # 서비스 응답을 처리하는 콜백 함수
        try:  # 응답 처리 중 예외를 잡기 위한 try 블록
            response = future.result()  # future 객체에서 서비스 응답 결과 가져오기
            self.get_logger().info(f'Result: {response.success}, {response.message}')  # 응답의 성공 여부와 메시지를 로그에 출력
        except Exception as e:  # 응답 처리 중 오류 발생 시 예외 처리
            self.get_logger().warn(f'{e}')  # 오류 메시지를 경고 로그로 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = AgvSpeedClientNode()  # AgvSpeedClientNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 서비스 요청 및 응답 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
