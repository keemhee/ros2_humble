#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.msg import NumForTest

class TestSubNode(Node):
    def __init__(self):
        super().__init__("test_sub")
        self.subscriber_ = self.create_subscription(NumForTest, "random_number", self.num_callback, 10)
        self.get_logger().info("sub node has been started.")

    def num_callback(self, msg):
        self.get_logger().info(f"{msg.random_number}")


def main(args=None):
    rclpy.init(args = args)
    node = TestSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()