# panther_description

URDF model of Panther robot

## Required plugins

panther_description package uses [hector_gazebo_plugins](http://wiki.ros.org/hector_gazebo_plugins) to simulate IMU and GPS.

## Configuring

### Xacro parameters

- `panther_common_props_path` *(default: [panther_common.yaml](./panther_description/config/panther_common.yaml))* - description of basic Panther parameters such as mass, inertia, torque, meshes and colors. Available colors are defined in [materials.urdf.xacro](./panther_description/urdf/materials.urdf.xacro).

- `wheel_props_path` *(default: [classic_wheels_props.yaml](./panther_description/config/classic_wheels_props.yaml))* - description of used wheel type.

- `use_gpu` *(default: false)* - sets LIDAR sensors to use GPU enabled gazebo plugin.


### Using different wheel types

Wheel type is determined by `wheel_props_path` parameter. Those YAML files define all physical properties of wheels and their gazebo plugin.

Predefined wheels:
- `WH01.yaml` - off-road skid drive wheels. Panther standard wheels

- `WH02.yaml` - mecanum wheels 

- `WH04.yaml` - small skid drive wheels

### Changing sensor configuration

Predefined sensors are:
- Orbbec Astra
- Slamtec RPLIDAR S1
- Velodyne Puck
- Ouster OS1 32

You can add those sensors defining them in [panther.urdf.xacro](./panther_description/urdf/panther.urdf.xacro). Defining Velodyne Puck would look as follows.
``` xml
<xacro:gazebo.velodyne_puck xyz="0.185 0 0.17" rpy="0 0 0" use_gpu="$(arg use_gpu)" />
```

You can define multiple sensors by changing parameters for both LIDAR sensors and camera `prefix` and `topic` for LIDAR sensors. This way you will avoid collisions in link names and topics.

For other depth cameras we suggest looking at official repositories:
- [Intel RealSense](https://github.com/IntelRealSense/realsense-ros)
- [Stereolabs ZED](https://github.com/stereolabs/zed-ros-wrapper)