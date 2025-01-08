#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_interfaces.action import Move

class MoveClientNode(Node):
    def __init__(self):
        super().__init__("move_client")
        self.client_=ActionClient(self, Move, 'move')
        self.get_logger().info("waiting for the server")

    def send_goal(self, distance):
        goal = Move.Goal()
        goal.distance = distance
        self.client_.wait_for_server()
        future = self.client_.send_goal_async(goal, feedback_callback=self.get_feedback_callback)
        future.add_done_callback(self.get_response_callback)

    def get_feedback_callback(self, feedback):
        feedback_msg = feedback.feedback
        self.get_logger().info(f'current distance: {feedback_msg.current_distance}')

    def get_response_callback(self, future):
        goal_handle=future.result()
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result_ = future.result().result
        try:
            self.get_logger().info(f'total distance: {result_.total_distance}')
        except Exception as e:
            self.get_logger().info(f'error: {e}')

def main(args=None):
    rclpy.init(args = args)
    node = MoveClientNode()
    node.send_goal(50.0)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()