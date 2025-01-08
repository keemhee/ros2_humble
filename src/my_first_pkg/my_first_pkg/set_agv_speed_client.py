#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.srv import Move

class AgvSpeedClientNode(Node):
    def __init__(self):
        super().__init__("set_agv_speed_client")
        self.client_=self.create_client(Move, 'set_agv_speed')
        while not self.client_.wait_for_service(timeout_sec=1):
            self.get_logger().info('Waiting for server')

        self.get_logger().info("client has been started.")
        self.call_service(1.0, 2.0)

    def call_service(self, x, z): 
        request = Move.Request()
        request.linear_velocity = x
        request.angular_velocity = z
        future = self.client_.call_async(request)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Result: {response.success}, {response.message}')
        except Exception as e:
            self.get_logger().warn(f'{e}')

def main(args=None):
    rclpy.init(args = args)
    node = AgvSpeedClientNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()