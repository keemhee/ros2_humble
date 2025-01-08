#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class RobotStationSubNode(Node):
    def __init__(self):
        super().__init__("sub_news")
        self.subscriber_=self.create_subscription(String, "robot_station3", self.news_callback, 10) #interface type, topic name, callback, queue size
        self.subscriber_count =self.create_subscription(Int32, "count_topic", self.count_callback, 1)
        self.get_logger().info("sub_news node has been started.")

    def news_callback(self, msg): 
        # print in terminal
        self.get_logger().info(msg.data)

    def count_callback(self, msg):
        self.get_logger().info(f"{msg.data}")


def main(args=None):
    rclpy.init(args = args)
    node = RobotStationSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()