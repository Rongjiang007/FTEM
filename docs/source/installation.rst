Installation
============

The PyQuake3D code is openly available on GitHub:

    https://github.com/Computational-Geophysics/PyQuake3D

We recommend using a Conda environment to manage dependencies.

Python Requirements
-------------------
PyQuake3D requires Python 3.8 or newer and the following libraries:

* numpy
* scipy
* matplotlib
* psutil
* mpi4py
* joblib
* h5py
* imageio
* pyvista

To install all dependencies, run:

.. code-block:: bash

   pip install -r requirements.txt

Or with Conda:

.. code-block:: bash

   conda env update -f environment.yml

GPU Acceleration (optional)
---------------------------
To enable GPU support, install ``cupy`` and the appropriate CUDA toolkit:

.. code-block:: bash

   conda install -c conda-forge cupy cudatoolkit=11.8

Notes:
* Ensure your NVIDIA GPU driver is compatible with the CUDA version.
* Check compatibility here: https://docs.cupy.dev/en/stable/install.html

C++ Requirements
----------------
PyQuake3D uses a C++ kernel for fast Green’s function evaluation.

* Source file: ``src/TDstressFS_C.cpp``
* Compiled into: ``TDstressFS_C.so``

To compile:

.. code-block:: bash

   cd src
   make

Dependencies on Linux:

.. code-block:: bash

   sudo apt update
   sudo apt install g++
   sudo apt install openmpi-bin libopenmpi-dev