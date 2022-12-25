#!/usr/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch CIT_DAR send_tips.launch.py > /tmp/CIT_DAR.log

cat /tmp/CIT_DAR.log |
grep 'ロボットシステム学'


