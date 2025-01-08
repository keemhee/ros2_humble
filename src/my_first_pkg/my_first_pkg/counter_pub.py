#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  #package.xml <depend>std_msgs</depend>

class MyCounterPub(Node):
    def __init__(self):
        super().__init__("counter_pub")
        self.get_logger().info("counter_pub node has been started.")
        time_period = 1    
        self.publisher_= self.create_publisher(Int32, "count_topic", 1) #(interface type, topic name, queue)
        self.create_timer(time_period, self.timer_callback)
        self.count=0

    def timer_callback(self):
        self.get_logger().info(f'current count: {self.count}')# for checking 
        msg = Int32()
        msg.data = self.count
        self.publisher_.publish(msg)
        self.count += 1


def main(args=None):
    rclpy.init(args = args)
    node = MyCounterPub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()