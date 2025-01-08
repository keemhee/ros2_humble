#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotStationNode(Node):
    def __init__(self):
        super().__init__("robot_station1")
        self.publisher_= self.create_publisher(String, "robot_station3", 10)
        period = 2
        self.create_timer(period, self.timer_callback)
        self.get_logger().info("robot_station has been started.")
    
    def timer_callback(self):
        msg = String()  #initiate
        msg.data = "Hi This is Kairos News Station"
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args = args)
    node = RobotStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()