#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.srv import Move
from geometry_msgs.msg import Twist

class SetAgvSpeedSubNode(Node):
    def __init__(self):
        super().__init__("set_agv_speed_sub")
        self.subscriber_ = self.create_subscription(Twist, "cmd_vel", self.agv_callback, 10)
        self.get_logger().info("set_agv_speed sub node has been started.")

    def agv_callback(self, msg):
        self.get_logger().info(f"x = {msg.linear.x}, z = {msg.angular.z} ")


def main(args=None):
    rclpy.init(args = args)
    node = SetAgvSpeedSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()