#!/usr/bin/env python3  # 이 스크립트를 Python 3로 실행하도록 지정

import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from nav_msgs.msg import OccupancyGrid  # OccupancyGrid 메시지 타입(2D 맵 데이터)을 가져옴
from geometry_msgs.msg import TransformStamped  # TF 변환 메시지 타입을 가져옴
import tf2_ros  # TF2 변환을 관리하기 위한 모듈 가져옴

class OccupancyGridNode(Node):  # OccupancyGridNode라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__("occupancy_pub")  # 노드 이름을 'occupancy_pub'로 설정하며 상위 클래스 초기화
        self.publisher_ = self.create_publisher(OccupancyGrid, "customed_occupancy_grid", 10)  # OccupancyGrid 메시지를 'customed_occupancy_grid' 토픽으로 발행할 퍼블리셔 생성, 큐 크기 10
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)  # TF 변환을 브로드캐스트하기 위한 객체 생성
        self.create_timer(1, self.occupancy_callback)  # 1초마다 occupancy_callback 함수를 호출하는 타이머 생성
        self.get_logger().info("publishing has been started")  # 노드 시작 메시지를 로그에 출력

    def occupancy_callback(self):  # 1초마다 호출되는 콜백 함수
        og = OccupancyGrid()  # OccupancyGrid 메시지 객체 생성
        og.header.stamp = self.get_clock().now().to_msg()  # 현재 시간을 메시지 헤더의 타임스탬프로 설정
        og.header.frame_id = 'map'  # 맵 데이터의 좌표 프레임을 'map'으로 설정
        og.info.resolution = 1.0  # 그리드 셀의 해상도를 1.0m로 설정 (각 셀 크기)
        og.info.width = 3  # 그리드의 너비를 3셀로 설정
        og.info.height = 3  # 그리드의 높이를 3셀로 설정 (3x3 맵)
        og.info.origin.position.x = 0.0  # 맵 원점의 x 위치를 0.0으로 설정
        og.info.origin.position.y = 0.0  # 맵 원점의 y 위치를 0.0으로 설정
        og.info.origin.position.z = 0.0  # 맵 원점의 z 위치를 0.0으로 설정
        og.info.origin.orientation.x = 0.0  # 맵 원점의 방향(x)을 0.0으로 설정 (쿼터니언)
        og.info.origin.orientation.y = 0.0  # 맵 원점의 방향(y)을 0.0으로 설정 (쿼터니언)
        og.info.origin.orientation.z = 0.0  # 맵 원점의 방향(z)을 0.0으로 설정 (쿼터니언)
        og.info.origin.orientation.w = 1.0  # 맵 원점의 방향(w)을 1.0으로 설정 (회전 없음)
        og.data = [0, 20, 40, 60, 80, 100, 80, 60, 40]  # 3x3 그리드의 셀 값 설정 (0: 빈 공간, 100: 장애물)

        self.publisher_.publish(og)  # OccupancyGrid 메시지를 토픽으로 발행

        tf_stamp = TransformStamped()  # TF 변환 메시지 객체 생성
        tf_stamp.header.stamp = self.get_clock().now().to_msg()  # 현재 시간을 TF 헤더의 타임스탬프로 설정
        tf_stamp.header.frame_id = 'map'  # 부모 프레임을 'map'으로 설정
        tf_stamp.child_frame_id = 'map_frame'  # 자식 프레임을 'map_frame'으로 설정
        tf_stamp.transform.translation.x = 0.0  # x 방향 이동을 0.0으로 설정
        tf_stamp.transform.translation.y = 0.0  # y 방향 이동을 0.0으로 설정
        tf_stamp.transform.translation.z = 0.0  # z 방향 이동을 0.0으로 설정
        tf_stamp.transform.rotation.x = 0.0  # 회전(x)을 0.0으로 설정 (쿼터니언)
        tf_stamp.transform.rotation.y = 0.0  # 회전(y)을 0.0으로 설정 (쿼터니언)
        tf_stamp.transform.rotation.z = 0.0  # 회전(z)을 0.0으로 설정 (쿼터니언)
        tf_stamp.transform.rotation.w = 1.0  # 회전(w)을 1.0으로 설정 (회전 없음)

        self.tf_broadcaster.sendTransform(tf_stamp)  # TF 변환 메시지를 브로드캐스트

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = OccupancyGridNode()  # OccupancyGridNode 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 발행 대기
    node.destroy_node()  # 노드 종료 및 리소스 정리
    rclpy.shutdown()  # ROS2 환경 종료

if __name__=="__main__":  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
