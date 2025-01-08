#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_interfaces.action import CountUntil

class CountUntilClientNode(Node):
    def __init__(self):
        super().__init__("count_until_client")
        self.client_=ActionClient(self, CountUntil, 'count_until')
        self.get_logger().info("Waiting for the server")
    
    def send_goal(self, target_number, period):
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = period
        self.client_.wait_for_server()

        future = self.client_.send_goal_async(goal, feedback_callback=self.feedback_callback)
        future.add_done_callback(self.get_response_callback)

    def feedback_callback(self, feedback):
        feedback_msg = feedback.feedback
        self.get_logger().info(f'current number: {feedback_msg.current_number}')


    def get_response_callback(self, future):
        goal_handle = future.result()
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result_= future.result().result
        try:
            self.get_logger().info(f'reached number: {result_.reached_number}')
        except Exception as e:
            self.get_logger().info(f'error: {e}')




def main(args=None):
    rclpy.init(args = args)
    node = CountUntilClientNode()
    node.send_goal(5, 1.0)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()