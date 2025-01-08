'''#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class IMGSubNode(Node):
    def __init__(self):
        super().__init__("img_sub")
        self.subscriber_=self.create_subscription(Image, 'img_raw', self.img_callback, 10)

        self.bridge = CvBridge()

        self.get_logger().info("sub node has been started.")

    def img_callback(self, img_data):
        frame = self.bridge.imgmsg_to_cv2(img_data, 'bgr8')
        cv2.imshow('Image', frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args = args)
    node = IMGSubNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()
    '''

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge

class IMGSubNode(Node):
    def __init__(self):
        super().__init__("img_sub")
        self.subscriber_ = self.create_subscription(Image, 'img_raw', self.img_callback, 10)
        self.bridge = CvBridge()
        self.get_logger().info("sub node has been started.")

    def img_callback(self, img_data):
        frame = self.bridge.imgmsg_to_cv2(img_data, 'bgr8')
        
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define range of red color in HSV
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        
        # Create a mask for red color
        mask = cv2.inRange(hsv, lower_red, upper_red)
        
        # Bitwise-AND mask and original image
        red_only = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Display the resulting frame
        cv2.imshow('Red Detection', red_only)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = IMGSubNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
