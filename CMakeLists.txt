cmake_minimum_required(VERSION 3.5)
project(panther_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY meshes urdf config rviz worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_package()