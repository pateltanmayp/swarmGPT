# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/jack/.local/lib/python3.8/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/jack/.local/lib/python3.8/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build

# Include any dependencies generated for this target.
include crazyflie_tools/CMakeFiles/comCheck.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include crazyflie_tools/CMakeFiles/comCheck.dir/compiler_depend.make

# Include the progress variables for this target.
include crazyflie_tools/CMakeFiles/comCheck.dir/progress.make

# Include the compile flags for this target's objects.
include crazyflie_tools/CMakeFiles/comCheck.dir/flags.make

crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.o: crazyflie_tools/CMakeFiles/comCheck.dir/flags.make
crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.o: /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src/crazyflie_tools/src/comCheck.cpp
crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.o: crazyflie_tools/CMakeFiles/comCheck.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.o"
	cd /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.o -MF CMakeFiles/comCheck.dir/src/comCheck.cpp.o.d -o CMakeFiles/comCheck.dir/src/comCheck.cpp.o -c /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src/crazyflie_tools/src/comCheck.cpp

crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/comCheck.dir/src/comCheck.cpp.i"
	cd /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src/crazyflie_tools/src/comCheck.cpp > CMakeFiles/comCheck.dir/src/comCheck.cpp.i

crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/comCheck.dir/src/comCheck.cpp.s"
	cd /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src/crazyflie_tools/src/comCheck.cpp -o CMakeFiles/comCheck.dir/src/comCheck.cpp.s

# Object files for target comCheck
comCheck_OBJECTS = \
"CMakeFiles/comCheck.dir/src/comCheck.cpp.o"

# External object files for target comCheck
comCheck_EXTERNAL_OBJECTS =

/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck: crazyflie_tools/CMakeFiles/comCheck.dir/src/comCheck.cpp.o
/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck: crazyflie_tools/CMakeFiles/comCheck.dir/build.make
/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck: /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/libcrazyflie_cpp.so
/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck: /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.71.0
/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck: /usr/lib/x86_64-linux-gnu/libusb-1.0.so
/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck: crazyflie_tools/CMakeFiles/comCheck.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck"
	cd /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/comCheck.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
crazyflie_tools/CMakeFiles/comCheck.dir/build: /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/devel/lib/crazyflie_tools/comCheck
.PHONY : crazyflie_tools/CMakeFiles/comCheck.dir/build

crazyflie_tools/CMakeFiles/comCheck.dir/clean:
	cd /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools && $(CMAKE_COMMAND) -P CMakeFiles/comCheck.dir/cmake_clean.cmake
.PHONY : crazyflie_tools/CMakeFiles/comCheck.dir/clean

crazyflie_tools/CMakeFiles/comCheck.dir/depend:
	cd /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/src/crazyflie_tools /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools /home/jack/DSL/crazyflie_repos/crazyswarm/ros_ws/build/crazyflie_tools/CMakeFiles/comCheck.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : crazyflie_tools/CMakeFiles/comCheck.dir/depend
