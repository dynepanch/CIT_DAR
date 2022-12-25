#!/usr/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source ~/.bashrc
timeout 10 ros2 launch CIT_DAR send_tips.launch.py > /tmp/CIT_DAR.log

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


