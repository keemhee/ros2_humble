#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class CounterPubTest(Node):
    def __init__(self):
        super().__init__("counter_pub")
        self.publisher_=self.create_publisher(Int32, "counter_pub", 1)
        self.create_timer(1, self.counter_callback)
        self.get_logger().info("test started")
        self.count = 0

    def counter_callback(self):
        count = Int32()
        count.data = self.count
        self.publisher_.publish(count)
        self.count += 1
        self.get_logger().info(f'current count: {count.data}')

def main(args=None):
    rclpy.init(args = args)
    node = CounterPubTest()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()