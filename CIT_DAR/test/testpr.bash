#!/usr/bin/bash
#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

source $dir/.bashrc

cd $dir/ros2_ws/src

git clone https://github.com/dynepanch/person_msgs.git

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

ros2 interface show "person_msgs/srv/Query"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

timeout 30 ros2 launch CIT_DAR send_tips.launch.py > /tmp/CIT_DAR.log

cat /tmp/CIT_DAR.log |
	grep 'ロボットシステム学'

cat /tmp/CIT_DAR.log |
	grep '信号処理論'

cat /tmp/CIT_DAR.log |
	grep 'ロボットマニピレータ'

cat /tmp/CIT_DAR.log |
	grep 'センサ工学'

cat /tmp/CIT_DAR.log |
	grep '設計制作'

