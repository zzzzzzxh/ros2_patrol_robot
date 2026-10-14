import launch
import launch_ros

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    # 获取urdf文件所在路径
    urdf_package_path = get_package_share_directory(
        'fishbot_description'
    )

    # 拼接urdf完整路径
    default_urdf_path = os.path.join(
        urdf_package_path,
        'urdf',
        'first_robot.urdf'
    )

    default_rviz_config_path = os.path.join(
        urdf_package_path,
        'config',
        'display_robot_model.rviz'
    )


    # 声明model参数，可以启动时修改urdf路径
    action_declare_arg_model_path = launch.actions.DeclareLaunchArgument(
        name='model',
        default_value=str(default_urdf_path),
        description='urdf文件的绝对路径'
    )


    # 读取urdf文件内容
    robot_description_content = launch.substitutions.Command(
        [
            'xacro ',
            launch.substitutions.LaunchConfiguration('model')
        ]
    )


    # 转换成robot_description参数
    robot_description_value = launch_ros.parameter_descriptions.ParameterValue(
        robot_description_content,
        value_type=str
    )


    # 启动robot_state_publisher
    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description': robot_description_value
            }
        ]
    )#传节点参数


    # 启动joint_state_publisher
    action_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
        
    )


    # 启动rviz2
    action_rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d',default_rviz_config_path]
    )#传路径


    # 返回所有启动动作
    return launch.LaunchDescription(
        [
            action_declare_arg_model_path,
            action_robot_state_publisher,
            action_joint_state_publisher,
            action_rviz_node
        ]
    )