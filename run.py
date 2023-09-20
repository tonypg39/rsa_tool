import docker 
import os
import argparse

pc_cmd = """
/home/tony/Documents/software/ros_docker/gui-docker -it --rm ur10dev:v1 /bin/bash

# to be added automatically to the .bashrc
source /opt/ros/noetic/setup.bash
source ~/ws_moveit/devel/setup.bash

# start the gazebo with the launch file
roslaunch ur_gazebo ur10_bringup.launch
roslaunch ur10_moveit_config moveit_planning_execution.launch sim:=true
roslaunch ur10_moveit_config moveit_rviz.launch config:=true
# RViz Tips:
# - Set the global frame (the first) to base_link, it is a select
# - Add a motion planning component, and it automatically connects to the robot
"""


if __name__ == "__main__":
    
    cmdline = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    cmdline.add_argument('--name', default="")
    cmdline.add_argument('--id', default="")
    cnt_name = "generic"
    cmd_base = f"/home/tony/Documents/software/ros_docker/gui-docker --name {cnt_name} ur10dev:v1 roslaunch ur_gazebo ur10_bringup.launch"
    os.popen(cmd_base)
    # gz = "roslaunch ur_gazebo ur10_bringup.launch"
    # os.popen("docker exec generic 'roslaunch ur_gazebo ur10_bringup.launch'")


