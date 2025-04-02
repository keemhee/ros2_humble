import serial  # 시리얼 통신을 위한 모듈을 가져옴
from geometry_msgs.msg import Twist  # ROS2에서 속도 명령 메시지(Twist)를 가져옴
import rclpy  # ROS2 Python 클라이언트 라이브러리를 가져옴
from rclpy.node import Node  # ROS2 노드 클래스를 가져옴

class TeleopToSerial(Node):  # TeleopToSerial 클래스를 정의하며 Node를 상속받음
    def __init__(self):  # 클래스의 생성자 함수 정의
        super().__init__('teleop_to_serial')  # 부모 클래스(Node)의 생성자를 호출하며 노드 이름을 'teleop_to_serial'로 설정
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # 시리얼 포트를 '/dev/ttyUSB0'로 설정, 속도 9600, 타임아웃 1초
        self.subscription = self.create_subscription(  # 'cmd_vel' 토픽을 구독하기 위한 서브스크립션 생성
            Twist,  # 메시지 타입을 Twist로 지정
            'cmd_vel',  # 구독할 토픽 이름 'cmd_vel' 설정
            self.listener_callback,  # 메시지가 도착하면 호출할 콜백 함수 지정
            10  # QoS 설정으로 메시지 큐 크기를 10으로 지정
        )

    def listener_callback(self, msg):  # 'cmd_vel' 토픽에서 메시지를 받았을 때 실행되는 콜백 함수
        linear = msg.linear.x  # Twist 메시지에서 선속도(x축)를 추출
        angular = msg.angular.z  # Twist 메시지에서 각속도(z축)를 추출

        if linear > 0:  # 선속도가 양수이면 (전진)
            self.serial_port.write(b'{"cmd":"i"}\n')  # 시리얼 포트로 전진 명령어({"cmd":"i"})를 전송
        elif linear < 0:  # 선속도가 음수이면 (후진)
            self.serial_port.write(b'{"cmd":"m"}\n')  # 시리얼 포트로 후진 명령어({"cmd":"m"})를 전송
        elif angular > 0:  # 각속도가 양수이면 (좌회전)
            self.serial_port.write(b'{"cmd":"j"}\n')  # 시리얼 포트로 좌회전 명령어({"cmd":"j"})를 전송
        elif angular < 0:  # 각속도가 음수이면 (우회전)
            self.serial_port.write(b'{"cmd":"l"}\n')  # 시리얼 포트로 우회전 명령어({"cmd":"l"})를 전송
        elif linear == 0 and angular == 0:  # 선속도와 각속도가 모두 0이면 (정지)
            self.serial_port.write(b'{"cmd":"k"}\n')  # 시리얼 포트로 정지 명령어({"cmd":"k"})를 전송

def main(args=None):  # 프로그램의 메인 함수 정의, args는 ROS2 인자 전달용
    rclpy.init(args=args)  # ROS2 환경을 초기화
    node = TeleopToSerial()  # TeleopToSerial 노드 객체 생성
    rclpy.spin(node)  # 노드를 실행하며 메시지 수신 대기
    rclpy.shutdown()  # ROS2 환경 종료

if __name__ == '__main__':  # 이 파일이 직접 실행될 때만 아래 코드 실행
    main()  # 메인 함수 호출
