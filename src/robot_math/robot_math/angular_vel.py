#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import sys
from geometry_msgs.msg import Twist

class AngularVelocityNode(Node):
    def __init__(self):
        super().__init__("Node_name")
        self.publisher_= self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_timer(0.1, self.angular_callback)
        self.get_logger().info("node has been started.")

    def angular_callback(self):
        msg = Twist()
        # w = v/r
        msg.linear.x = float(sys.argv[1]) #vel
                                          #radius = float(sys.argv[2])
        msg.angular.z = msg.linear.x / float(sys.argv[2])
        self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args = args)
    node = AngularVelocityNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()