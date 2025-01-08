#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_=self.create_service(AddTwoInts, 'add_two_ints', self.add_callback)
        self.get_logger().info("server has been started.")

    def add_callback(self, request, response):
        '''a = request.a
        b = request.b
        response.sum = a + b'''
        response.sum = request.a + request.b
        self.get_logger().info(f'{request.a} + {request.b} = {response.sum}')
        return response


def main(args=None):
    rclpy.init(args = args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()