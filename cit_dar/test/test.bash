#!/usr/bin/bash
#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch cit_dar send_tips.launch.py > /tmp/cit_dar.log

cat /tmp/cit_dar.log |
grep 'ロボットシステム学'

cat /tmp/cit_dar.log |
grep '信号処理論'

cat /tmp/cit_dar.log |
grep 'ロボットマニピレータ'

cat /tmp/cit_dar.log |
grep 'センサ工学'

cat /tmp/cit_dar.log |
grep '設計制作'


