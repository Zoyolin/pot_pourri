cmake_minimum_required(VERSION 3.10)

# add_subdirectory(somelib)
set(TARGET ps1_shortener.run)
set(hello true CACHE STRING "No hello here")
add_executable(${TARGET} ps1_shortener.cpp)
target_include_directories(${TARGET} PRIVATE include)


get_filename_component(PRJPATH "${CMAKE_PROJECT_DIR}"
                       REALPATH BASE_DIR "${CMAKE_BINARY_DIR}")
message( ${PRJPATH})

project(ps1_shortener)

add_custom_target(run
    COMMAND ${TARGET}
    DEPENDS ps1_shortener
    WORKING_DIRECTORY ${CMAKE_PROJECT_DIR}
)