#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from my_interfaces.srv import Move

class AgvSpeedControllerNode(Node):
    def __init__(self):
        super().__init__("set_agv_speed")
        self.publisher_= self.create_publisher(Twist, 'cmd_vel', 10)
        self.server_=self.create_service(Move, 'set_agv_speed', self.speed_callback)
        self.twist = Twist()
        self.twist.linear.x = 3.0
        self.twist.angular.z = 1.5
        self.create_timer(1, self.controller_callback)
        self.get_logger().info("agv speed controller has been started. linear velocity = 3.0, angular velocity = 1.5")

    def controller_callback(self):
        self.publisher_.publish(self.twist)

    def speed_callback(self, request, response):
        self.twist.linear.x = request.linear_velocity
        self.twist.angular.z = request.angular_velocity
        response.success = True
        response.message = 'speed changed.'
        self.get_logger().info(f'new linear velocity = {self.twist.linear.x}, new angular velocity = {self.twist.angular.z}')

        return response

def main(args=None):
    rclpy.init(args = args)
    node = AgvSpeedControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()