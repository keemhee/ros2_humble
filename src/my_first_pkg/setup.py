from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*.launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kim',
    maintainer_email='kim@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'counter_node = my_first_pkg.my_first_node:main',
            'counter_pub = my_first_pkg.counter_pub:main',
            'robot_station2 = my_first_pkg.robot_station:main',
            'sub_sub = my_first_pkg.news_sub:main',
            'turtle_pose = my_first_pkg.turtlesim_pose_sub:main',
            'turtle_color = my_first_pkg.turtlesim_color_sub:main',
            'turtlesim_pub = my_first_pkg.turtlesim_pub:main',
            'turtlesim_controller = my_first_pkg.turtlesim_controller:main',
            'add_two_ints_server = my_first_pkg.add_two_ints_server:main',
            'add_two_ints_client = my_first_pkg.add_two_ints_client:main',
            'add_three_ints_server = my_first_pkg.add_three_ints_server:main',
            'add_three_ints_client = my_first_pkg.add_three_ints_client:main',
            'sensor_status_pub = my_first_pkg.sensor_status_pub:main',
            'sensor_status_sub = my_first_pkg.sensor_status_sub:main',
            'set_agv_speed_controller = my_first_pkg.set_agv_speed_controller:main',
            'set_agv_speed_client = my_first_pkg.set_agv_speed_client:main',
            'set_agv_speed_sub = my_first_pkg.set_agv_speed_sub:main',
            'count_until_server = my_first_pkg.count_until_server:main',
            'count_until_client = my_first_pkg.count_until_client:main',
            'move_server = my_first_pkg.move_server:main',
            'move_client = my_first_pkg.move_client:main',
            'number_pub_for_test = my_first_pkg.number_pub_for_test:main',
            'number_sub_for_test = my_first_pkg.number_sub_for_test:main'
        ],
    },
)
