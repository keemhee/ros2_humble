from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    counter_pub = Node(package = 'my_first_pkg',
                   executable = 'counter_node', #it's not a publisher==> use counter_pub
                   name = 'counter',
                   namespace = 'counterPub')
    counter_sub = Node(package = 'my_first_pkg',
                   executable = 'sub_sub',
                   name = 'counter',
                   namespace = 'counterSub')

    ld.add_action(counter_pub)
    ld.add_action(counter_sub)


    return ld