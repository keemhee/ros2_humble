import serial
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node

class TeleopToSerial(Node):
    def __init__(self):
        super().__init__('teleop_to_serial')
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # 포트 설정
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        linear = msg.linear.x
        angular = msg.angular.z

        if linear > 0:
            self.serial_port.write(b'{"cmd":"i"}\n')  # 전진
        elif linear < 0:
            self.serial_port.write(b'{"cmd":","}\n')  # 후진
        elif angular > 0:
            self.serial_port.write(b'{"cmd":"j"}\n')  # 좌회전
        elif angular < 0:
            self.serial_port.write(b'{"cmd":"l"}\n')  # 우회전
        elif linear == 0 and angular == 0:
            self.serial_port.write(b'{"cmd":"k"}\n')  # 정지

def main(args=None):
    rclpy.init(args=args)
    node = TeleopToSerial()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
