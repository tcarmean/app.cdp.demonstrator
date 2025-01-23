cmake_minimum_required(VERSION 3.15)
project(demonstrator)

include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)
conan_basic_setup()

add_executable(demonstrator src/demonstrator.c)
find_package(module_a REQUIRED)
find_package(module_b REQUIRED)
target_link_libraries(demonstrator module_a::module_a module_b::module_b)
