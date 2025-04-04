#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from rclpy.action import ActionClient  # ROS2 액션 클라이언트를 위한 모듈 가져옴
from my_interfaces.action import Move  # 사용자 정의 Move 액션 타입을 가져옴

class MoveClientNode(Node):  # MoveClientNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("move_client")  # 노드 이름을 'move_client'로 설정하며 상위 클래스 초기화
        self.client_ = ActionClient(self, Move, 'move')  # 'move' 액션 서버와 통신할 클라이언트 생성
        self.get_logger().info("waiting for the server")  # 서버 대기 메시지를 로그에 출력

    def send_goal(self, distance):  # 액션 목표를 전송하는 함수, 이동 거리를 인자로 받음
        goal = Move.Goal()  # Move 액션의 목표 객체 생성
        goal.distance = distance  # 이동할 거리를 설정 (예: 50.0)
        self.client_.wait_for_server()  # 액션 서버가 준비될 때까지 대기
        future = self.client_.send_goal_async(goal, feedback_callback=self.get_feedback_callback)  # 비동기적으로 목표 전송, 피드백 콜백 지정
        future.add_done_callback(self.get_response_callback)  # 목표 전송 완료 시 호출할 콜백 함수 등록

    def get_feedback_callback(self, feedback):  # 액션 피드백을 처리하는 콜백 함수
        feedback_msg = feedback.feedback  # 피드백 메시지에서 데이터 추출
        self.get_logger().info(f'current distance: {feedback_msg.current_distance}')  # 현재 이동 거리를 로그에 출력

    def get_response_callback(self, future):  # 목표 전송 응답을 처리하는 콜백 함수
        goal_handle = future.result()  # 목표 전송 결과(goal_handle) 가져오기
        result_future = goal_handle.get_result_async()  # 비동기적으로 최종 결과 요청
        result_future.add_done_callback(self.get_result_callback)  # 결과 수신 완료 시 호출할 콜백 함수 등록

    def get_result_callback(self, future):  # 최종 결과를 처리하는 콜백 함수
        result_ = future.result().result  # 액션의 최종 결과 가져오기
        try:  # 결과 처리 중 예외를 잡기 위한 try 블록
            self.get_logger().info(f'total distance: {result_.total_distance}')  # 총 이동 거리를 로그에 출력
        except Exception as e:  # 결과 처리 중 오류 발생 시 예외 처리
            self.get_logger().info(f'error: {e}')  # 오류 메시지를 로그에 출력

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = MoveClientNode()  # MoveClientNode 객체 생성
    node.send_goal(50.0)  # 이동 거리 50.0으로 액션 목표 전송
    rclpy.spin(node)  # 노드를 실행하며 액션 요청 및 응답 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
