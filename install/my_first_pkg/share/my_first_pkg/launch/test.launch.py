from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtle1 = Node(
        package = 'turtlesim',
        executable = 'turtlesim_node',
        namespace = 'turtlesim1',
        name = 'sim',
        parameters = [{'background_r' : 200}])
    turtle2 = Node(
        package = 'turtlesim',
        executable = 'turtlesim_node',
        namespace = 'turtlesim2',
        # = 'turtle_teleop_key',
        name = 'sim')
    mimic = Node(
        package = 'turtlesim',
        executable = 'mimic',
        name = 'mimic',
        remappings = [
            ('/input/pose', '/turtlesim1/turtle1/pose'),
            ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel')]) #original, changed
    ld.add_action(turtle1)
    ld.add_action(turtle2)
    ld.add_action(mimic)

    return ld