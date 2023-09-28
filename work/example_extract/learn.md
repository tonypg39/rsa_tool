## The structure of the launch file

```
<launch>

--- Define args
--- Include the world.launch (Probably starts the world)

--- Spawn the URDF in gazebo (using the package gazebo_ros)
    - First create a parameter with the urdf
    - use the command *spawn_urdf* to spawn it 

--- Includes controller_utlis and creates nodes for starting the controllers

<launch>

```

