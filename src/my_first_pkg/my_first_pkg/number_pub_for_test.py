#!/usr/bin/env python3

import random
import rclpy
from rclpy.node import Node
from my_interfaces.msg import NumForTest

class TestPubNode(Node):
    def __init__(self):
        super().__init__("test_pub")
        self.publisher_ = self.create_publisher(NumForTest, "random_number", 10)
        self.create_timer(1, self.timer_callback)
        self.get_logger().info("pub node has been started.")

    def timer_callback(self):
        num = random.randint(1, 100)
        msg = NumForTest()
        msg.random_number = num
        self.publisher_.publish(msg)
        self.get_logger().info(f'number: {msg.random_number}')


def main(args=None):
    rclpy.init(args = args)
    node =TestPubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()