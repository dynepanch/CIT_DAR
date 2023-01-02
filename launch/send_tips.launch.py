#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import time
def generate_launch_description():
    send = launch_ros.actions.Node(
        package='cit_dar',
        executable='send',
    )
    time.sleep(5) 
    tips = launch_ros.actions.Node(
        package='cit_dar',
        executable='tips',
        output='screen'
    )

    return launch.LaunchDescription([send, tips])

