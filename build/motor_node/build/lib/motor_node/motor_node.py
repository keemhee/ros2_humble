import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelSubscriber(Node):
    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,  # 메시지 타입
            '/cmd_vel',  # 토픽 이름
            self.cmd_vel_callback,  # 콜백 함수
            10  # 큐 크기
        )
        self.subscription  # 방지: 콜백 해제가 될 수 있으므로 저장
        self.get_logger().info('node has been started.')

    def cmd_vel_callback(self, msg):
        linear = msg.linear
        angular = msg.angular
        
        self.get_logger().info(
            f'Received /cmd_vel: Linear - x: {linear.x}, y: {linear.y}, z: {linear.z} | '
            f'Angular - x: {angular.x}, y: {angular.y}, z: {angular.z}'
        )

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
