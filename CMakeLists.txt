cmake_minimum_required(VERSION 3.15)
project(demonstrator)

# Print the value of CMAKE_SOURCE_DIR for debugging
message(STATUS "CMAKE_SOURCE_DIR: ${CMAKE_SOURCE_DIR}")

add_executable(demonstrator src/demonstrator.c)
find_package(module_a CONFIG REQUIRED)
find_package(module_b CONFIG REQUIRED)
target_link_libraries(demonstrator module_a::module_a module_b::module_b)

# Print include directories for debugging
get_target_property(demonstrator_INCLUDE_DIRS demonstrator INCLUDE_DIRECTORIES)
message(STATUS "Include Directories: ${demonstrator_INCLUDE_DIRS}")

