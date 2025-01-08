#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.msg import SensorStatus

class SensorStatusSubNode(Node):
    def __init__(self):
        super().__init__("sensor_status_sub")
        self.subscriber_ = self.create_subscription(SensorStatus, "sensor_status", self.motor_callback, 10)
        self.get_logger().info("sensor status sub node has been started.")

    def motor_callback(self, msg):
        self.get_logger().info(f"{msg.debug_messages}")


def main(args=None):
    rclpy.init(args = args)
    node = SensorStatusSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()