#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import time  # 시간 지연을 위한 모듈 가져옴
import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from rclpy.action import ActionServer  # ROS2 액션 서버를 위한 모듈 가져옴
from rclpy.action.server import ServerGoalHandle  # 액션 서버의 목표 핸들 타입 가져옴
from my_interfaces.action import Move  # 사용자 정의 Move 액션 타입을 가져옴

class MoveServerNode(Node):  # MoveServerNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("move_server")  # 노드 이름을 'move_server'로 설정하며 상위 클래스 초기화
        self.server_ = ActionServer(self, Move, 'move', self.execute_callback)  # 'move' 액션 서버를 생성하고 목표 처리 콜백 지정
        self.get_logger().info("server node has been started")  # 서버 시작 메시지를 로그에 출력

    def execute_callback(self, goal_handle: ServerGoalHandle):  # 액션 목표를 처리하는 콜백 함수, 목표 핸들을 인자로 받음
        distance = goal_handle.request.distance  # 클라이언트 요청에서 이동 거리 추출
        feedback = Move.Feedback()  # 피드백 메시지 객체 생성
        #total_distance = 0  # 총 이동 거리를 저장할 변수 (주석 처리된 원래 코드)
        current_distance = 0.0  # 현재 이동 거리를 저장할 변수 초기화

        '''for i in range(5):  # 5번 반복하며 이동 시뮬레이션 (주석 처리된 원래 코드)
            total_distance += distance  # 목표 거리를 반복적으로 더함 (주석 처리된 원래 코드)
            feedback.current_distance = total_distance  # 현재 거리를 피드백에 설정 (주석 처리된 원래 코드)
            goal_handle.publish_feedback(feedback)  # 피드백을 클라이언트에 전송 (주석 처리된 원래 코드)
            time.sleep(1)  # 1초 대기 (주석 처리된 원래 코드)
            '''
        while current_distance < distance:  # 현재 거리가 목표 거리에 도달할 때까지 반복
            current_distance += 10.0  # 1초마다 10.0 단위로 이동 거리 증가
            feedback.current_distance = current_distance  # 현재 거리를 피드백에 설정
            goal_handle.publish_feedback(feedback)  # 피드백을 클라이언트에 전송
            time.sleep(1)  # 1초 대기

        goal_handle.succeed()  # 목표가 성공적으로 완료되었음을 표시
        self.get_logger().info('moved successfully')  # 이동 완료 메시지를 로그에 출력

        result = Move.Result()  # 결과 메시지 객체 생성
        result.total_distance = current_distance  # 총 이동 거리를 결과에 설정
        return result  # 결과 객체를 클라이언트에 반환

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = MoveServerNode()  # MoveServerNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 액션 요청 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
