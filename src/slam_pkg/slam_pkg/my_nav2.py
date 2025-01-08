#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped, PoseStamped

class MyNavGoalNode(Node):
    def __init__(self):
        super().__init__("my_nav_goal")
        self.subscriber_=self.create_subscription(PointStamped, "clicked_point", self.point_callback, 10)
        self.publisher_=self.create_publisher(PoseStamped, "goal_pose", 10)
        self.get_logger().info("node has been started.")

    def point_callback(self, msg):
        goal_pose1=PoseStamped()
        goal_pose1.pose.x = msg.point.x
        goal_pose1.pose.y = msg.point.y
        goal_pose1.pose.z = msg.point.z
        
        self.publisher_.publish(goal_pose1)

def main(args=None):
    rclpy.init(args = args)
    node = MyNavGoalNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()