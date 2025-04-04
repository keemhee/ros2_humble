#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from rclpy.action import ActionClient  # ROS2 액션 클라이언트를 위한 모듈 가져옴
from my_interfaces.action import CountUntil  # 사용자 정의 CountUntil 액션 타입을 가져옴

class CountUntilClientNode(Node):  # CountUntilClientNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("count_until_client")  # 노드 이름을 'count_until_client'로 설정하며 상위 클래스 초기화
        self.client_ = ActionClient(self, CountUntil, 'count_until')  # 'count_until' 액션 서버와 통신할 클라이언트 생성
        self.get_logger().info("Waiting for the server")  # 서버 대기 메시지를 로그에 출력
    
    def send_goal(self, target_number, period):  # 액션 목표를 전송하는 함수, 목표 숫자와 주기를 인자로 받음
        goal = CountUntil.Goal()  # CountUntil 액션의 목표 객체 생성
        goal.target_number = target_number  # 목표 숫자를 설정 (예: 5)
        goal.period = period  # 카운트 주기를 설정 (예: 1.0초)
        self.client_.wait_for_server()  # 액션 서버가 준비될 때까지 대기
        future = self.client_.send_goal_async(goal, feedback_callback=self.feedback_callback)  # 비동기적으로 목표 전송, 피드백 콜백 지정
        future.add_done_callback(self.get_response_callback)  # 목표 전송 완료 시 호출할 콜백 함수 등록

    def feedback_callback(self, feedback):  # 액션 피드백을 처리하는 콜백 함수
        feedback_msg = feedback.feedback  # 피드백 메시지에서 데이터 추출
        self.get_logger().info(f'current number: {feedback_msg.current_number}')  # 현재 카운트 숫자를 로그에 출력

    def get_response_callback(self, future):  # 목표 전송 응답을 처리하는 콜백 함수
        goal_handle = future.result()  # 목표 전송 결과(goal_handle) 가져오기
        result_future = goal_handle.get_result_async()  # 비동기적으로 최종 결과 요청
        result_future.add_done_callback(self.get_result_callback)  # 결과 수신 완료 시 호출할 콜백 함수 등록

    def get_result_callback(self, future):  # 최종 결과를 처리하는 콜백 함수
        result_ = future.result().result  # 액션의 최종 결과 가져오기
        try:  # 결과 처리 중 예외를 잡기 위한 try 블록
            self.get_logger().info(f'reached number: {result_.reached_number}')  # 도달한 숫자를 로그에 출력
        except Exception as e:  # 결과 처리 중 오류 발생 시 예외 처리
            self.get_logger().info(f'error: {e}')  # 오류 메시지를 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = CountUntilClientNode()  # CountUntilClientNode 객체 생성
    node.send_goal(5, 1.0)  # 목표 숫자 5와 주기 1.0초로 액션 목표 전송
    rclpy.spin(node)  # 노드를 실행하며 액션 요청 및 응답 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
