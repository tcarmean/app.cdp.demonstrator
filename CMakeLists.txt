cmake_minimum_required(VERSION 3.15)
project(demonstrator)

# Print the value of CMAKE_SOURCE_DIR for debugging
message(STATUS "CMAKE_SOURCE_DIR: ${CMAKE_SOURCE_DIR}")

include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)

add_executable(demonstrator src/demonstrator.c)
find_package(module_a REQUIRED)
find_package(module_b REQUIRED)
target_link_libraries(demonstrator module_a::module_a module_b::module_b)
