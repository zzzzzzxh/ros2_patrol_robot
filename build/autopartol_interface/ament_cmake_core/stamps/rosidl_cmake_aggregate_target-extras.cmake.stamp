# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target autopartol_interface::autopartol_interface
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${autopartol_interface_TARGETS}.
if(autopartol_interface_TARGETS AND NOT TARGET autopartol_interface::autopartol_interface)
  add_library(autopartol_interface::autopartol_interface INTERFACE IMPORTED)
  set_target_properties(autopartol_interface::autopartol_interface PROPERTIES
    INTERFACE_LINK_LIBRARIES "${autopartol_interface_TARGETS}")
endif()
