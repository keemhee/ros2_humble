#!/usr/bin/env python3

import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from my_interfaces.action import CountUntil

class CountUntilServerNode(Node):
    def __init__(self):
        super().__init__("count_until_server")
        self.server_=ActionServer(self, CountUntil, 'count_until', self.execute_callback)
        self.get_logger().info("server has been started.")

    def execute_callback(self, goal_handle:ServerGoalHandle):
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period
        feedback = CountUntil.Feedback()
        
        for count in range(target_number+1):
            #time.sleep(period)
            #self.get_logger().info(f'{count}')      ->feedback
            feedback.current_number = count
            goal_handle.publish_feedback(feedback)
            time.sleep(period)

        goal_handle.succeed()
        self.get_logger().info('action completed successfully')

        result = CountUntil.Result()
        result.reached_number = target_number 

        return result

def main(args=None):
    rclpy.init(args = args)
    node = CountUntilServerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()