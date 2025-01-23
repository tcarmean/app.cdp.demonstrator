cmake_minimum_required(VERSION 3.15)
project(demonstrator)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(demonstrator src/demonstrator.c)
target_link_libraries(demonstrator ${CONAN_LIBS})