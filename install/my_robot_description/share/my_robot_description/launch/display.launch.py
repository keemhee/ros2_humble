
from launch import LaunchDescription
from launch_ros.actions import Node 
from ament_index_python.packages import get_package_share_directory
import os 

def generate_launch_description():
    
    package_directory = get_package_share_directory('my_robot_description')
    urdf_file = os.path.join(package_directory, 
                             'urdf',
                             'urdf_for_test.urdf')
    config_file=os.path.join(package_directory, 'config', 'rviz_config_for_test.rviz')
    
    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'            
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',           
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]

        ),
        Node(
            package='rviz2',
            executable='rviz2',  
            output='screen',
            arguments=['-d', config_file]       
        )
    ])