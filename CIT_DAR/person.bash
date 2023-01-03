#!/usr/bin/bash
#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws/src

ros2 pkg create --build-type ament_cmake person_msgs

cd persom_msgs

cat person_Cmake > Cmake.txt
cat person_pac > package.xml

mkdir srv

cd srv

cat Query > Query.srv

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 interface show person_msgs/srv/Query

