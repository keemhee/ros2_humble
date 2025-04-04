#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import time  # 시간 지연을 위한 모듈 가져옴
import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from rclpy.action import ActionServer  # ROS2 액션 서버를 위한 모듈 가져옴
from rclpy.action.server import ServerGoalHandle  # 액션 서버의 목표 핸들 타입 가져옴
from my_interfaces.action import CountUntil  # 사용자 정의 CountUntil 액션 타입을 가져옴

class CountUntilServerNode(Node):  # CountUntilServerNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("count_until_server")  # 노드 이름을 'count_until_server'로 설정하며 상위 클래스 초기화
        self.server_ = ActionServer(self, CountUntil, 'count_until', self.execute_callback)  # 'count_until' 액션 서버를 생성하고 목표 처리 콜백 지정
        self.get_logger().info("server has been started.")  # 서버 시작 메시지를 로그에 출력

    def execute_callback(self, goal_handle: ServerGoalHandle):  # 액션 목표를 처리하는 콜백 함수, 목표 핸들을 인자로 받음
        target_number = goal_handle.request.target_number  # 클라이언트 요청에서 목표 숫자 추출
        period = goal_handle.request.period  # 클라이언트 요청에서 주기 추출
        feedback = CountUntil.Feedback()  # 피드백 메시지 객체 생성
        
        for count in range(target_number + 1):  # 0부터 목표 숫자까지 반복
            #time.sleep(period)  # 주기만큼 대기 (주석 처리된 원래 코드)
            #self.get_logger().info(f'{count}')  # 카운트 값을 로그에 출력 (주석 처리된 원래 코드 -> 피드백으로 대체)
            feedback.current_number = count  # 현재 카운트 값을 피드백에 설정
            goal_handle.publish_feedback(feedback)  # 피드백을 클라이언트에 전송
            time.sleep(period)  # 지정된 주기만큼 대기

        goal_handle.succeed()  # 목표가 성공적으로 완료되었음을 표시
        self.get_logger().info('action completed successfully')  # 액션 완료 메시지를 로그에 출력

        result = CountUntil.Result()  # 결과 메시지 객체 생성
        result.reached_number = target_number  # 도달한 숫자를 결과에 설정
        return result  # 결과 객체를 클라이언트에 반환

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = CountUntilServerNode()  # CountUntilServerNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 액션 요청 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
