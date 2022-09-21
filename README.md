# panther_description

## Installation

This package relates to other repositories that have to be build from source. It also requires user to select which Gazebo one want to use. To select Gazebo vertion run:
``` bash
# For Ignition Gazebo
export GAZEBO_VERSION=ignition-gazebo
# For Gazebo Classic
export GAZEBO_VERSION=gazebo-classic
```
``` bash
vcs import < components.repos src
rosdep update --rosdistro $ROS_DISTRO
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
colcon build
```

## Usage

Basic Panther configuration can be found in file [panther.urdf.xacro](./panther_description/urdf/panther.urdf.xacro). This is example configuration showing how to use the model. This can be used to import in launch files as a base line model. For more advanced usecases [panther_macro.urdf.xacro](./panther_description/urdf/panther_macro.urdf.xacro) is designed to be integrated into custom robot configurations.

## Parameters

Arguments passed to the [panther.urdf.xacro](./panther_description/urdf/panther.urdf.xacro) are the same as parameters of [panther_macro.urdf.xacro](./panther_description/urdf/panther_macro.urdf.xacro) thus this section covers both of them.


- `use_sim` *(default: false)* - Changes between *ros2_control* for simulation and hardware **[TO BE IMPLEMENTED]**.
- `dual_bat` *(default: false)* - Changes inertia and mass for robot body to match 2 batteries setup.
- `imu_pos_x` *(default: 0.169)* - **x** coordinate of IMU sensor in relation to `body_link`.
- `imu_pos_y` *(default: 0.025)* - **y** coordinate of IMU sensor in relation to `body_link`.
- `imu_pos_z` *(default: 0.092)* - **z** coordinate of IMU sensor in relation to `body_link`.
- `imu_rot_r` *(default: 0.0 )* - roll rotation of IMU sensor in relation to `body_link`.
- `imu_rot_p` *(default: 0.0)* - pitch rotation of IMU sensor in relation to `body_link`.
- `imu_rot_y`  *(default: 0.0)* - yaw rotation of IMU sensor in relation to `body_link`.
- `wheel_props_path` *(default: $(find panther_description)/config/WH01.yaml)* - absolute path to YAML file defining wheel properties.
- `simulation_engine` *(default: gazebo-classic)* - physics engine to select plugins for. Supported engines: `gazebo-classic` **[MORE ENGINES TO BE IMPLEMENTED]**.

There is one additional [panther.urdf.xacro](./panther_description/urdf/panther.urdf.xacro) argument:
- `use_gpu` *(default: false)* - Turns on GPU acceleration for sensors.
It is not present in the [panther_macro.urdf.xacro](./panther_description/urdf/panther_macro.urdf.xacro) since base of a robot does not have any sensors that can be accelerated with GPU.

Parameter `wheel_props_path` allows to use non standard wheels with Panther robot without modyfying URDF file. Syntax is following:
- `mass` - wheel mass in **[Kg]**.
- `inertia` - diagonal of inertia tensor in **[Kg m^2]**. required subfileds:
  - `ixx` - inertia alongside axis **x**.
  - `iyy` - inertia alongside axis **y**.
  - `izz` - inertia alongside axis **z**.
- `inertia_y_offset` - Offset of center of mass in **y** direction in **[m]**.
- `diameter` - wheel diameter.
- `wheel_separation` - separation of wheels alongisde *y* axis.
- `mesh_package` - ROS package name to search for custom meshes. Used in evaluation **$(find my_amazing_package)/**.
- `folder_path` - path used to search for mesh files within ROS package.
- `kinematics` - kinematics type. Possible options: `differential`, `mecanum`.

Wheels have to be named as follows:
- `collision.stl` - wheel collision mesh.
- `wheel_a.dae` - front, left wheel visual mesh.
- `wheel_b.dae` - front, right wheel visual mesh.
- `wheel_c.dae` - rear, left wheel visual mesh.
- `wheel_d.dae` - rear, right wheel visual mesh.


## Sensor configuration

Sensors are defined in [husarion/ros_components_description](https://github.com/husarion/ros_components_description) repository. Which is downloaded by VCS in the installation step. Guide on how to combine those sensors with the robot will be written soon.