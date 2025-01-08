#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class IMGPubNode(Node):
    def __init__(self):
        super().__init__("img_pub")
        self.publisher_=self.create_publisher(Image, 'img_raw', 10)
        self.create_timer(0.1, self.img_callback)

        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()

        self.get_logger().info("pub node has been started")

    def img_callback(self):
        ret, frame = self.cap.read()
        img_data = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
        
        self.publisher_.publish(img_data)

def main(args=None):
    rclpy.init(args = args)
    node = IMGPubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()