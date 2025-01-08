#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Color

class TurtlesimColorSubNode(Node):
    def __init__(self):
        super().__init__("turtle_color")
        self.subscriber_=self.create_subscription(Color,
                                                  "/turtle1/color_sensor",
                                                  self.color_callback, 10)
        self.get_logger().info("turtle color node has been started.")

    def color_callback(self, color):
        self.get_logger().info(f"r: {color.r},g: {color.g}, b: {color.b}")


def main(args=None):
    rclpy.init(args = args)
    node = TurtlesimColorSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()