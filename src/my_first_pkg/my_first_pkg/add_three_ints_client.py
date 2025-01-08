
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.srv import AddThreeInts

class AddThreeIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_three_ints_client")
        self.client_=self.create_client(AddThreeInts, 'add_three_ints')
        while not self.client_.wait_for_service(timeout_sec=1):
            self.get_logger().info('Waiting for server')

        self.get_logger().info("client has been started.")
        self.call_add_two_ints_service(1, 2, 3)

    def call_add_two_ints_service(self, a, b, c):
        request = AddThreeInts.Request()
        request.a = a
        request.b = b
        request.c = c
        future = self.client_.call_async(request)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Result: {response.sum}')
        except Exception as e:
            self.get_logger().warn(f'{e}')

def main(args=None):
    rclpy.init(args = args)
    node = AddThreeIntsClientNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()