from setuptools import find_packages, setup

package_name = 'fishbot_applacation'

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
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "init_robot_pose=fishbot_applacation.init_robot_pose:main",
            "get_robot_pose=fishbot_applacation.get_robot_pose:main",
            "nav_to_pose=fishbot_applacation.nav_to_pose:main",
            "waypoint_follow=fishbot_applacation.waypoint_follow:main",
        ],
    },
)
