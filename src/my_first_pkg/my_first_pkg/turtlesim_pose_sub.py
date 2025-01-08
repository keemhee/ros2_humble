#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtlesimPoseSubNode(Node):
    def __init__(self):
        super().__init__("turtle_pose")
        self.subscriber_=self.create_subscription(Pose,
                                                  "/turtle1/pose",
                                                  self.pose_callback, 10)
        self.get_logger().info("turtle pose node has been started.")

    '''
    def pose_callback(self, msg):
        self.get_logger().info(f"x: {msg.x},y: {msg.y}, theta: {msg.theta},
                               linear velocity: {msg.linear_velocity},
                               angular velocity: {msg.angular_velocity}")
                               '''
    def pose_callback(self, pose):
        pass
        #self.get_logger().info(f"x: {pose.x},y: {pose.y}, theta: {pose.theta},
        #                       linear velocity: {pose.linear_velocity},
        #                       angular velocity: {pose.angular_velocity}")


def main(args=None):
    rclpy.init(args = args)
    node = TurtlesimPoseSubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()