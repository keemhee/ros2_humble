    #!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import TransformStamped
import tf2_ros

class OccupancyGridNode(Node):
    def __init__(self):
        super().__init__("occupancy_pub")
        self.publisher_= self.create_publisher(OccupancyGrid, "customed_occupancy_grid", 10)
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        self.create_timer(1, self.occupancy_callback)
        self.get_logger().info("publishing has been started")

    def occupancy_callback(self):
        og = OccupancyGrid()
        og.header.stamp = self.get_clock().now().to_msg()
        og.header.frame_id = 'map'
        og.info.resolution = 1.0
        og.info.width = 3
        og.info.height = 3
        og.info.origin.position.x = 0.0
        og.info.origin.position.y = 0.0
        og.info.origin.position.z = 0.0
        og.info.origin.orientation.x = 0.0
        og.info.origin.orientation.y = 0.0
        og.info.origin.orientation.z = 0.0
        og.info.origin.orientation.w = 1.0
        og.data = [0, 20, 40, 60, 80, 100, 80, 60, 40]  # 0 ~ 100

        self.publisher_.publish(og)

        tf_stamp = TransformStamped()
        tf_stamp.header.stamp = self.get_clock().now().to_msg()
        tf_stamp.header.frame_id = 'map'
        tf_stamp.child_frame_id = 'map_frame'
        tf_stamp.transform.translation.x = 0.0
        tf_stamp.transform.translation.y = 0.0
        tf_stamp.transform.translation.z = 0.0
        tf_stamp.transform.rotation.x = 0.0
        tf_stamp.transform.rotation.y = 0.0
        tf_stamp.transform.rotation.z = 0.0
        tf_stamp.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(tf_stamp) 


def main(args=None):
    rclpy.init(args = args)
    node = OccupancyGridNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()