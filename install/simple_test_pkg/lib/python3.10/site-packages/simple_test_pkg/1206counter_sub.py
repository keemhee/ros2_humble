#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class CounterSubTest(Node):
    def __init__(self):
        super().__init__("counter_sub")
        self.subscriber_=self.create_subscription(Int32, "counter_pub", self.counter_sub_callback, 1)
        self.get_logger().info("test started")

    def counter_sub_callback(self, count):
        self.get_logger().info(f'current count: {count.data}')

def main(args=None):
    rclpy.init(args = args)
    node = CounterSubTest()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()