import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class CmdVelSubscriber(Node):
    def __init__(self):
        super().__init__('cmd_vel_subscriber')

        # 시리얼 포트 초기화
        try:
            self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
            self.get_logger().info('Serial port opened successfully.')
        except serial.SerialException as e:
            self.get_logger().error(f'Failed to open serial port: {e}')
            self.serial_port = None

        # /cmd_vel 구독 설정
        self.subscription = self.create_subscription(
            Twist,  # 메시지 타입
            '/cmd_vel',  # 토픽 이름
            self.cmd_vel_callback,  # 콜백 함수
            10  # 큐 크기
        )
        self.subscription  # 방지: 콜백 해제가 될 수 있으므로 저장
        self.get_logger().info('Node has been started.')

    def cmd_vel_callback(self, msg):
        linear = msg.linear
        angular = msg.angular
        
        # 메시지 수신 로그
        self.get_logger().info(
            f'Received /cmd_vel: Linear - x: {linear.x}, y: {linear.y}, z: {linear.z} | '
            f'Angular - x: {angular.x}, y: {angular.y}, z: {angular.z}'
        )
        
        # 시리얼 데이터 전송
        if self.serial_port and self.serial_port.is_open:
            '''data = f'Linear: {linear.x:.2f}, {linear.y:.2f}, {linear.z:.2f}; ' \
                   f'Angular: {angular.x:.2f}, {angular.y:.2f}, {angular.z:.2f}\n'
            '''
            data = 'a'
            try:
                self.serial_port.write(data.encode('utf-8'))
                self.get_logger().info(f'Sent to serial: {data.strip()}')
            except serial.SerialException as e:
                self.get_logger().error(f'Failed to send data over serial: {e}')

    def destroy_node(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.get_logger().info('Serial port closed.')
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
