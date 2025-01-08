from setuptools import find_packages, setup

package_name = 'motor_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'motor_node = motor_node.motor_node:main',
            'motor_node2 = motor_node.motor_node2:main',
            'moving_rc_car = motor_node.rccar_stm32:main'
        ],
    },
)
