import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # ROS2의 Twist 메시지 타입(속도 데이터)을 가져옴

class CmdVelSubscriber(Node):  # CmdVelSubscriber라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__('cmd_vel_subscriber')  # 노드 이름을 'cmd_vel_subscriber'로 설정하며 상위 클래스 초기화
        self.subscription = self.create_subscription(  # 토픽 구독 객체 생성
            Twist,  # 구독할 메시지 타입 (Twist)
            '/cmd_vel',  # 구독할 토픽 이름
            self.cmd_vel_callback,  # 메시지 수신 시 호출할 콜백 함수
            10  # 메시지 큐 크기 (최대 10개 메시지 대기)
        )
        self.subscription  # 구독 객체를 유지 (파이썬 가비지 컬렉션 방지용, 실제로는 불필요한 줄)
        self.get_logger().info('node has been started.')  # 노드 시작 완료 메시지를 로그에 출력

    def cmd_vel_callback(self, msg):  # cmd_vel 토픽 메시지를 처리하는 콜백 함수
        linear = msg.linear  # Twist 메시지에서 선속도(linear) 데이터를 추출
        angular = msg.angular  # Twist 메시지에서 각속도(angular) 데이터를 추출
        
        self.get_logger().info(  # 수신한 속도 데이터를 로그로 출력
            f'Received /cmd_vel: Linear - x: {linear.x}, y: {linear.y}, z: {linear.z} | '  # 선속도 x, y, z 값 출력
            f'Angular - x: {angular.x}, y: {angular.y}, z: {angular.z}'  # 각속도 x, y, z 값 출력
        )

def main(args=None):  # 프로그램의 메인 함수
    rclpy.init(args=args)  # ROS2 환경 초기화
    node = CmdVelSubscriber()  # CmdVelSubscriber 노드 객체 생성
    try:  # 노드 실행 시도
        rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    except KeyboardInterrupt:  # Ctrl+C로 종료 시 예외 처리
        pass  # 아무 동작 없이 넘어감
    finally:  # 종료 시 항상 실행
        node.destroy_node()  # 노드 종료 및 리소스 정리
        rclpy.shutdown()  # ROS2 환경 종료

if __name__ == '__main__':  # 스크립트가 직접 실행될 때만 main 함수 호출
    main()  # 메인 함수 실행
