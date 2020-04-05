# 3D_PC_visualizer

In this repository there is the code for a Point Cloud object visualizer using the Open3D library

## Installation

1. Create a Python3 virtual environment and activate it.
2. Install Open3D library
   1. `git clone --recursive https://github.com/intel-isl/Open3D`.
   2. `cd Opem3D && mkdir build && cd build `.
   3. `cmake ..`.
   4. **Ubuntu:** `make -j$(nproc)` / **Mac OS:** `make -j$(sysctl -n hw.physicalcpu)`.
   5. `make install-pip-package`.
   
### Note: 
If you are going to use the visualizer from Mac OS, before installing the Open3D library, you must update TCL / Tk and the Python version of the system. This is because the Python that comes by default with Mac OS has a very old version of TCL / TK and proper operation of tkinter is not allowed. To do this, follow these steps:
1. Download and install Python version 3.8.2 from the official website www.python.org.
2. Download and install the new version of TCL / TK from [here](https://www.activestate.com/products/tcl/).
3. Create the Python environment with the new Python's version.
