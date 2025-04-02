import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # ROS2의 Twist 메시지 타입(속도 데이터)을 가져옴
import serial  # 시리얼 통신을 위한 모듈을 가져옴

class CmdVelSubscriber(Node):  # CmdVelSubscriber라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__('cmd_vel_subscriber')  # 노드 이름을 'cmd_vel_subscriber'로 설정하며 상위 클래스 초기화

        # 시리얼 포트 초기화
        try:  # 시리얼 포트 열기를 시도
            self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # '/dev/ttyUSB0' 포트를 9600 보드레이트로 열기, 타임아웃 1초
            self.get_logger().info('Serial port opened successfully.')  # 성공 시 로그에 메시지 출력
        except serial.SerialException as e:  # 시리얼 포트 열기 실패 시 예외 처리
            self.get_logger().error(f'Failed to open serial port: {e}')  # 실패 시 오류 메시지 로그 출력
            self.serial_port = None  # 시리얼 포트 객체를 None으로 설정

        # /cmd_vel 구독 설정
        self.subscription = self.create_subscription(  # 토픽 구독 객체 생성
            Twist,  # 구독할 메시지 타입 (Twist)
            '/cmd_vel',  # 구독할 토픽 이름
            self.cmd_vel_callback,  # 메시지 수신 시 호출할 콜백 함수
            10  # 메시지 큐 크기 (최대 10개 메시지 대기)
        )
        self.subscription  # 구독 객체를 유지 (파이썬 가비지 컬렉션 방지용, 실제로는 불필요한 줄)
        self.get_logger().info('Node has been started.')  # 노드 시작 완료 메시지를 로그에 출력

    def cmd_vel_callback(self, msg):  # cmd_vel 토픽 메시지를 처리하는 콜백 함수
        linear = msg.linear  # Twist 메시지에서 선속도(linear) 데이터를 추출
        angular = msg.angular  # Twist 메시지에서 각속도(angular) 데이터를 추출
        
        # 메시지 수신 로그
        self.get_logger().info(  # 수신한 속도 데이터를 로그로 출력
            f'Received /cmd_vel: Linear - x: {linear.x}, y: {linear.y}, z: {linear.z} | '  # 선속도 x, y, z 값 출력
            f'Angular - x: {angular.x}, y: {angular.y}, z: {angular.z}'  # 각속도 x, y, z 값 출력
        )
        
        # 시리얼 데이터 전송
        if self.serial_port and self.serial_port.is_open:  # 시리얼 포트가 열려 있는지 확인
            '''data = f'Linear: {linear.x:.2f}, {linear.y:.2f}, {linear.z:.2f}; ' \  # 주석 처리된 원래 데이터 형식 (속도 값 전송)
                   f'Angular: {angular.x:.2f}, {angular.y:.2f}, {angular.z:.2f}\n'
            '''
            data = 'a'  # 현재는 단순히 'a'라는 문자열을 전송하도록 설정
            try:  # 시리얼 데이터 전송 시도
                self.serial_port.write(data.encode('utf-8'))  # 데이터를 UTF-8로 인코딩하여 시리얼 포트로 전송
                self.get_logger().info(f'Sent to serial: {data.strip()}')  # 전송 성공 시 로그 출력
            except serial.SerialException as e:  # 전송 실패 시 예외 처리
                self.get_logger().error(f'Failed to send data over serial: {e}')  # 실패 시 오류 메시지 로그 출력

    def destroy_node(self):  # 노드 종료 시 호출되는 메서드
        if self.serial_port and self.serial_port.is_open:  # 시리얼 포트가 열려 있으면
            self.serial_port.close()  # 시리얼 포트를 닫음
            self.get_logger().info('Serial port closed.')  # 포트 닫힘을 로그에 출력
        super().destroy_node()  # 상위 클래스의 노드 종료 메서드 호출

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


'''
import rclpy  # ROS2 파이썬 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴
from geometry_msgs.msg import Twist  # ROS2의 Twist 메시지 타입(속도 데이터)을 가져옴
import serial  # 시리얼 통신을 위한 모듈을 가져옴

class CmdVelSubscriber(Node):  # CmdVelSubscriber라는 ROS2 노드 클래스를 정의
    def __init__(self):  # 노드 초기화 메서드
        super().__init__('cmd_vel_subscriber')  # 노드 이름을 'cmd_vel_subscriber'로 설정하며 상위 클래스 초기화

        # 시리얼 포트 초기화
        try:  # 시리얼 포트 열기를 시도
            self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # '/dev/ttyUSB0' 포트를 9600 보드레이트로 열기
            self.get_logger().info('Serial port opened successfully.')  # 성공 시 로그에 메시지 출력
        except serial.SerialException as e:  # 시리얼 포트 열기 실패 시 예외 처리
            self.get_logger().error(f'Failed to open serial port: {e}')  # 실패 시 오류 메시지 로그 출력
            self.serial_port = None  # 시리얼 포트 객체를 None으로 설정

        # /cmd_vel 구독 설정
        self.subscription = self.create_subscription(  # 토픽 구독 객체 생성
            Twist,  # 구독할 메시지 타입 (Twist)
            '/cmd_vel',  # 구독할 토픽 이름
            self.cmd_vel_callback,  # 메시지 수신 시 호출할 콜백 함수
            10  # 메시지 큐 크기 (최대 10개 메시지 대기)
        )
        self.get_logger().info('Node has been started.')  # 노드 시작 완료 메시지를 로그에 출력

    def cmd_vel_callback(self, msg):  # cmd_vel 토픽 메시지를 처리하는 콜백 함수
        linear_x = msg.linear.x  # 선속도 x 값 (앞/뒤 이동)
        angular_z = msg.angular.z  # 각속도 z 값 (회전)

        # 수신한 속도 데이터 로그 출력
        self.get_logger().info(f'Received /cmd_vel: Linear.x={linear_x:.2f}, Angular.z={angular_z:.2f}')

        # 시리얼 데이터 전송
        if self.serial_port and self.serial_port.is_open:  # 시리얼 포트가 열려 있는지 확인
            try:  # 시리얼 데이터 전송 시도
                if linear_x > 0:  # 선속도가 양수일 때 (전진)
                    data = '{"cmd":"i"}\n'  # 전진 명령
                elif linear_x < 0:  # 선속도가 음수일 때 (후진)
                    data = '{"cmd":"m"}\n'  # 후진 명령
                elif angular_z > 0:  # 각속도가 양수일 때 (좌회전)
                    data = '{"cmd":"j"}\n'  # 좌회전 명령
                elif angular_z < 0:  # 각속도가 음수일 때 (우회전)
                    data = '{"cmd":"l"}\n'  # 우회전 명령
                else:  # 선속도와 각속도가 모두 0일 때 (정지)
                    data = '{"cmd":"k"}\n'  # 정지 명령

                self.serial_port.write(data.encode('utf-8'))  # 명령을 UTF-8로 인코딩하여 시리얼 포트로 전송
                self.get_logger().info(f'Sent to serial: {data.strip()}')  # 전송한 명령 로그 출력
            except serial.SerialException as e:  # 전송 실패 시 예외 처리
                self.get_logger().error(f'Failed to send data over serial: {e}')  # 실패 시 오류 메시지 로그 출력

    def destroy_node(self):  # 노드 종료 시 호출되는 메서드
        if self.serial_port and self.serial_port.is_open:  # 시리얼 포트가 열려 있으면
            self.serial_port.close()  # 시리얼 포트를 닫음
            self.get_logger().info('Serial port closed.')  # 포트 닫힘을 로그에 출력
        super().destroy_node()  # 상위 클래스의 노드 종료 메서드 호출

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
    '''
