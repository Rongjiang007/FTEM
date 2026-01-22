Tutorials
=========

We provide Jupyter notebooks and example datasets to help new users get started.

Getting Started
---------------
A step-by-step installation and run guide is available here:

https://github.com/Computational-Geophysics/PyQuake3D/blob/main/tutorials

This notebook walks through:

* Setting up the environment
* Compiling the C++ extension
* Configuring input geometry and parameter files
* Running a benchmark BP5-QD rupture simulation

Running Simulations
-------------------
Simulations can be run from the root of the project.

**Standard single CPU/GPU mode:**

.. code-block:: bash

   python src/main.py -g <input_geometry_file> -p <input_parameter_file>

Example:

.. code-block:: bash

   python src/main_gpu.py -g examples/BP5-QD/bp5t.msh -p examples/BP5-QD/parameter.txt

**MPI parallel mode (recommended for large problems):**

.. code-block:: bash

   mpirun -n 4 python src/main_mpi.py -g <input_geometry_file> -p <input_parameter_file>

Post-Processing
---------------
Results can be visualized with `PyVista` or exported to VTK for analysis.

For more details, see Section 5 of the User Manual.