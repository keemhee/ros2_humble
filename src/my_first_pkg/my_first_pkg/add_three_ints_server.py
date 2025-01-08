#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.srv import AddThreeInts

class AddThreeIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_three_ints_server")
        self.server_=self.create_service(AddThreeInts, 'add_three_ints', self.add_callback)
        self.get_logger().info("server has been started.")

    def add_callback(self, request, response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info(f'{request.a} + {request.b} + {request.c} = {response.sum}')
        return response


def main(args=None):
    rclpy.init(args = args)
    node = AddThreeIntsServerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()