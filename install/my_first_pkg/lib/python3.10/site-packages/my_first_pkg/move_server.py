#!/usr/bin/env python3

import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from my_interfaces.action import Move

class MoveServerNode(Node):
    def __init__(self):
        super().__init__("move_server")
        self.server_=ActionServer(self, Move, 'move', self.execute_callback)
        self.get_logger().info("server node has been started")

    def execute_callback(self, goal_handle:ServerGoalHandle):
        distance = goal_handle.request.distance
        feedback = Move.Feedback()
        #total_distance = 0
        current_distance = 0.0

        '''for i in range(5):
            total_distance += distance
            feedback.current_distance = total_distance
            goal_handle.publish_feedback(feedback)
            time.sleep(1)
            '''
        while current_distance < distance:
            current_distance += 10.0
            feedback.current_distance = current_distance
            goal_handle.publish_feedback(feedback)
            time.sleep(1)

        goal_handle.succeed()
        self.get_logger().info('moved successfully')

        result = Move.Result()
        result.total_distance = current_distance

        return result

def main(args=None):
    rclpy.init(args = args)
    node = MoveServerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()