#!/usr/bin/env python3

import random
import rclpy
from rclpy.node import Node
from my_interfaces.msg import SensorStatus

class SensorStatusPubNode(Node):
    def __init__(self):
        super().__init__("sensor_status_pub")
        self.publisher_ = self.create_publisher(SensorStatus, "sensor_status", 10)
        self.create_timer(1, self.timer_callback)
        self.get_logger().info("sensor node has been started.")

    def timer_callback(self):
        tmp = random.randint(10, 50)
        msg = SensorStatus()
        msg.temerature = tmp
        if tmp > 30:
            msg.is_motor_ready = True
            msg.debug_messages ='motor is ready to move'
        else:
            msg.is_motor_ready = False
            msg.debug_messages ='not yet'
        self.publisher_.publish(msg)
        self.get_logger().info(f'current temp.: {msg.temerature}')


def main(args=None):
    rclpy.init(args = args)
    node = SensorStatusPubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()