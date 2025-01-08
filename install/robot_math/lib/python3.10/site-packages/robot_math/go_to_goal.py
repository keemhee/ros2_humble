#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys
import math

class GoToGoalNode(Node):
    def __init__(self):
        super().__init__("go_to_goal_node")
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.create_timer(0.1, self.go_to_goal)
        self.get_logger().info("Node has been started.")

    def pose_callback(self, data):
        self.pose = data

    def go_to_goal(self):
        goal = Pose()
        goal.x = float(sys.argv[1])
        goal.y = float(sys.argv[2])
        goal.theta = float(sys.argv[3])
        distance_tolerance = 0.1
        angle_tolerance = 0.01

        distance_to_goal = math.sqrt((goal.x - self.pose.x)**2 + (goal.y - self.pose.y)**2)
        angle_to_goal = math.atan2(goal.y - self.pose.y, goal.x - self.pose.x) - self.pose.theta

        self.get_logger().info(f"Remaining Distance: {distance_to_goal:.3f}, Remaining Angle: {angle_to_goal:.3f}")

        new_vel = Twist()
        if abs(angle_to_goal) > angle_tolerance:
            new_vel.angular.z = 5 * angle_to_goal
        elif distance_to_goal > distance_tolerance:
            new_vel.linear.x = 5 * distance_to_goal
        else:
            self.get_logger().info("Goal Reached")
            quit()

        self.publisher_.publish(new_vel)

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoalNode()
    rclpy.spin(node)
    node.destroy_node()

if __name__ == "__main__":
    main()
