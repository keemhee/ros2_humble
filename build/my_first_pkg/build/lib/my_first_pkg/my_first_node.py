#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyCounter(Node):
    def __init__(self):
        super().__init__("my_counter_node")
        self.get_logger().info("counting start")
        self.count = 0
        self.create_timer(1, self.callback_counter)
    
    def callback_counter(self):
        self.count += 1
        self.get_logger().info(f'current count: {self.count}')

def main(args=None):
    rclpy.init(args = args)
    node = MyCounter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()