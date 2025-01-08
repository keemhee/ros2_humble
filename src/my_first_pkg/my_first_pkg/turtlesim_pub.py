#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlesimPubNode(Node):
    def __init__(self):
        super().__init__("turtlesim_pub")
        self.get_logger().info("turtlesim pub node has been started.")
        time_period = 1    
        self.publisher_= self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_timer(time_period, self.pub_callback)

    def pub_callback(self):
        msg = Twist()    #msg can be other words. like twist=Twist() whatever
        msg.linear.x = 1.0 #bigger number, bigger circle
        #msg.linear.y = 0
        #msg.linear.z = 0
        #msg.angular.x = 0
        #msg.angular.y = 0
        msg.angular.z = 1.75
        self.publisher_.publish(msg)
        self.get_logger().info(f'x: {msg.linear.x}, theta: {msg.angular.z}')

def main(args=None):
    rclpy.init(args = args)
    node = TurtlesimPubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()