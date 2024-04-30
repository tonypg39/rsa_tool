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

gui_docker_path = "/home/pal/rosdev/"

if __name__ == "__main__":
    
    cmdline = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    cmdline.add_argument('--name', default="")
    cmdline.add_argument('--id', default="")
    cmdline.add_argument('--img_base', default="humble-dev:v1.0")
    # cmdline.add_argument('--empty', default="")
    cnt_name = "generic"

    # print(dck_cmd)
    flags, unk_args = cmdline.parse_known_args()
    f_id, f_name, f_img_base = flags.id, flags.name, flags.img_base
    if flags.name != "":
        cnt_name = flags.name
    cmd_reset = "docker rm -f generic"
    cmd_base = f"{gui_docker_path}gui-docker --network host --name {cnt_name} -it --entrypoint /bin/bash {f_img_base}"

    # Bring up Gazebo empty world with an arm (Discontinued)
    # cmd_base = f"{gui_docker_path}gui-docker --network host --name {cnt_name} {f_img_base} roslaunch ur_gazebo test3.launch"
    print(cmd_base)
    cmd_base = f'gnome-terminal -- bash -c "{cmd_base}; exec bash"'
    os.popen(cmd_reset)
    os.popen(cmd_base)


# docker cp 260de001e0b9:/opt/ros/noetic/share/ur_gazebo/launch/ur10_bringup.launch ./work/
# docker cp 260de001e0b9:/opt/ros/noetic/share/ur10_moveit_config/launch/moveit_planning_execution.launch ./work/
# docker cp 260de001e0b9:/opt/ros/noetic/share/ur10_moveit_config/launch/moveit_rviz.launch ./work/

# roslaunch ur_gazebo ur10_bringup.launch
# roslaunch ur10_moveit_config moveit_planning_execution.launch sim:=true
# roslaunch ur10_moveit_config moveit_rviz.launch config:=true
