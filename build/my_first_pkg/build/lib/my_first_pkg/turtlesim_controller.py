#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen

class TurtlesimControllerNode(Node):
    def __init__(self):
        super().__init__("turtlesim_controller")
        self.get_logger().info("turtlesim controller has been started.")
        self.subscriber_=self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.publisher_= self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.client_= self.create_client(SetPen, '/turtle1/set_pen')
        self.pose_=Pose()
        time_period = 0.1  
        self.create_timer(time_period, self.controller_callback)

    def send_request(self, r, g, b, width, off):
        self.request_= SetPen.Request()
        self.request_.r = r
        self.request_.g = g
        self.request_.b = b
        self.request_.width = width
        self.request_.off = off 
        self.client_.call_async(self.request_)

    def pose_callback(self, Pose):
        '''
        self.pose_.x = pose.x
        self.pose_.y = pose.y
        '''
        self.pose_ = Pose
        #self.get_logger().info(f"x: {Pose.x},y: {Pose.y}, theta: {Pose.theta}")
        
    def controller_callback(self):
        twist=Twist()

        if self.pose_.x < 1.0 or self.pose_.x > 10.5 or self.pose_.y < 1.0 or self.pose_.y > 10.5:
            twist.linear.x = 0.5
            twist.angular.z = 1.75
        else:
            twist.linear.x = 2.0
            twist.angular.z = 0.0

        self.publisher_.publish(twist)

        if self.pose_.x<5:
            self.send_request(0, 255, 0, 5, 0)
        else:
            self.send_request(255, 0, 0, 5, 0)



def main(args=None):
    rclpy.init(args = args)
    node = TurtlesimControllerNode()
    rclpy.spin(node)

    node.destroy_node()    
    rclpy.shutdown()

if __name__=="__main__":
    main()