from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    config_dir=os.path.join(get_package_share_directory('nav_pkg'), 'config')

    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            output='screen',
            arguments=['-configuration_directory', config_dir,
                       '-configuration_basename', 'turtlebot3_lds_2d.lua']
        ),
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            output='screen'
        )
    ])