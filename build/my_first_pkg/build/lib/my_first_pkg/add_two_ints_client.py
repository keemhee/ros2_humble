#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_=self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client_.wait_for_service(timeout_sec=1):
            self.get_logger().info('Waiting for server')

        self.get_logger().info("client has been started.")
        self.call_add_two_ints_service(4, 6) #set a(int64), b(int64)

    def call_add_two_ints_service(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client_.call_async(request) # future => result => response
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Result: {response.sum}')
        except Exception as e:
            self.get_logger().warn(f'{e}')

def main(args=None):
    rclpy.init(args = args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()