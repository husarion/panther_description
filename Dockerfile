FROM osrf/ros:noetic-desktop-full

# Use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update Ubuntu Software repository
RUN apt update && \
    apt upgrade -y

RUN apt install -y git \
    python3-dev \
    python3-pip \
    python3-rospkg \
    ros-$ROS_DISTRO-joint-state-publisher \
    ros-$ROS_DISTRO-ros-control \
    ros-$ROS_DISTRO-ros-controllers \
    ros-$ROS_DISTRO-hector-gazebo-plugins

# Python 3 dependencies
RUN pip3 install \
        rosdep \
        rospkg 

# Create and initialise ROS workspace
RUN mkdir -p /ros_ws/src
COPY ./src /ros_ws/src
WORKDIR /ros_ws
RUN mkdir build && \
    source /opt/ros/$ROS_DISTRO/setup.bash && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y && \
    catkin_make install

WORKDIR /

# Clear 
RUN apt clean && \
    rm -rf /var/lib/apt/lists/* 

COPY ./ros_entrypoint.sh /