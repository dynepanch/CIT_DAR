import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import time
def generate_launch_description():
    send = launch_ros.actions.Node(
        package='CIT_DAR',
        executable='send',
    )
    time.sleep(5) 
    tips = launch_ros.actions.Node(
        package='CIT_DAR',
        executable='tips',
        output='screen'
    )

    return launch.LaunchDescription([send, tips])

