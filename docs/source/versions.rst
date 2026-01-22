Versions
=========

v1.0.0 (2025-09-30)
-------------------

We are pleased to announce the first public release of **PyQuake3D** – a Python-based simulation framework for modeling 3-D earthquake sequences, capturing both seismic and aseismic fault slip.

Key Features
~~~~~~~~~~~~

- Simulation of multi-cycle earthquake behavior on 3-D faults
- Support for both seismic rupture and aseismic creep
- GPU acceleration using **CuPy**
- MPI parallelization for large-scale computations
- Modular finite-difference / finite-volume numerical implementation
- Geometry-based input using ``.msh`` files
- Parameter-driven simulation control (``parameter.txt``)
- Diagnostic output and visualization tools via HDF5 and Matplotlib
- Includes benchmark examples such as **SCEC BP5-QD**

Example Simulations
~~~~~~~~~~~~~~~~~~~

- `Planar Fault with Frictional Heterogeneity <https://www.youtube.com/watch?v=N_yA4uY77C0>`_
- `East Anatolian Fault Zone Model <https://www.youtube.com/watch?v=oFy3FSLs3UQ>`_


v1.0.1 (2025-10-06)
-------------------

**Release Summary**

Version **1.0.1** introduces major improvements in physics modeling, MPI scalability, and data handling.  
This update expands PyQuake3D’s ability to simulate fully coupled earthquake cycles while streamlining the MPI code structure and optimizing outputs for large-scale workflows.

**What’s Changed**

1. **Dilatancy Law Implementation**  
   PyQuake3D now includes a fully coupled **dilatancy law**.  
   The earthquake-cycle model combines 3-D elasticity, rate-and-state friction, and porosity evolution using a Boundary Integral Equation Method (BIEM) coupled to a Finite Difference Method (FDM).  
   Pore-fluid diffusion parallel to the fault is neglected. The FDM time-marching scheme is fully MPI-parallelized.

2. **Enhanced Modularity (MPI Version)**  
   The MPI version has been reorganized for clarity.  
   The main driver now uses only **six core functions**, simplifying the execution pipeline and improving maintainability.

3. **Comprehensive MPI Acceleration**  
   MPI is now applied to **all computational components**, beyond matrix–vector products and Green’s function evaluation.  
   This delivers improved scaling and faster performance on distributed-memory HPC systems.

4. **Optimized Output Format (VTU)**  
   Simulation output is now written in **VTU** format.  
   File sizes are reduced by approximately **threefold** compared to the previous VTK format, improving storage efficiency and I/O throughput.

5. **Updated `parameter.txt`**  
   Several parameter names related to stress and output configuration have been revised.  
   Users should update existing `parameter.txt` files to align with the new naming conventions.


v1.0.2 (2025-12-01)
-------------------

**Release Summary**

Version **1.0.2** introduces two major advancements to PyQuake3D:  
(1) a scalable **Lattice H-matrix** architecture for distributed-memory HPC systems, and  
(2) the implementation of **thermal pressurization**, enabling thermo–hydro–mechanical weakening during dynamic rupture.  
Together, these additions greatly enhance PyQuake3D’s capability to model multi-physics earthquake processes at scale.

**What’s Changed**

1. **Lattice H-matrix Implementation**

   PyQuake3D now includes a **Lattice H-matrix** framework, a distributed-memory extension of the standard H-matrix format designed for large-scale Boundary Element Method (BEM) simulations.

   Lattice H-matrices improve parallel scalability by organizing matrix blocks into a 2D MPI “lattice” layout, reducing communication overhead and enabling efficient compression and multiplication for extremely large, dense BEM matrices.

   *Context and Motivation*

   - In BEM, the stiffness matrix is fully dense, and matrix–vector products dominate computational cost.
   - Standard H-matrices compress these matrices but require **global MPI reductions** at each Runge–Kutta stage, leading to prohibitive communication cost as process count increases.
   - In PyQuake3D’s conventional H-matrix implementation, each time step requires:  
     1. dot products between local H-matrix subblocks and slip rates,  
     2. **MPI\_Reduce** to gather contributions across all ranks,  
     3. another **MPI\_Reduce** to compute global slip rates.

     Communication therefore scales like **O(n²)** with increasing MPI processes.

   *Lattice H-matrix Improvement*

   - Lattice H-matrices reorganize data into a **2D MPI grid**.  
   - Dot-product accumulation and slip-rate updates occur **locally within each MPI row**, independent of other rows.
   - Only diagonal processes perform global reductions at the end of RK stages.
   - This reduces communication complexity from **O(n²)** to **O(n)**.

   *Impact*

   - Greatly improved strong-scaling efficiency for large MPI jobs  
   - Lower communication overhead  
   - Faster time integration for large 3D earthquake-cycle models  
   - Enhanced suitability for Tier-1/Tier-0 supercomputers

2. **Thermal Pressurization**

   PyQuake3D now supports **thermal pressurization (TP)** as a dynamic weakening mechanism during seismic slip.

   During rapid coseismic slip, frictional heating raises pore fluid temperature, producing pore pressure that reduces effective normal stress and dramatically weakens the fault. This process can govern rupture speed, stress drop, and arrest behavior.

   The governing equations for pore fluid pressure :math:`p` and temperature :math:`T` follow :cite:`rice2006heating,noda2010three`:

   .. math::
      \frac{\partial p}{\partial t} = c_{hy} \frac{\partial^2 p}{\partial y^2} + \Lambda \frac{\partial T}{\partial t}
      :label: fluid_eqs1

   .. math::
      \frac{\partial T}{\partial t} = \alpha_{th} \frac{\partial^2 T}{\partial y^2} +
      \frac{\tau V \exp\left(-y^2 / (2 w^2)\right)}{\rho c \sqrt{2 \pi} w}
      :label: temp_eqs

with boundary conditions:

**Thermal pressurization only**

.. math::

    \left. \frac{\partial p}{\partial y} \right|_{y=0^+} = 0, \qquad
    \left. \frac{\partial T}{\partial y} \right|_{y=0^+} = 0

**Coupled dilatancy + thermal pressurization**

.. math::

    \left. \frac{\partial p}{\partial y} \right|_{y=0^+} =
    \frac{h \dot{\phi}}{2 \beta c_{hyd}}, \qquad
    \left. \frac{\partial T}{\partial y} \right|_{y=0^+} = 0

where:

   - :math:`T` — pore fluid temperature  
   - :math:`p` — pore pressure  
   - :math:`c_{hy}` — hydraulic diffusivity  
   - :math:`\alpha_{th}` — thermal diffusivity  
   - :math:`w` — shear zone half-width  
   - :math:`\rho c` — volumetric heat capacity  
   - :math:`\Lambda` — thermal pressurization coefficient  
   - :math:`\tau V` — frictional heating source term distributed across the shear zone

   *Physical Interpretation*

   - **Dilatancy** increases porosity → decreases pore pressure → strengthens the fault.  
   - **Thermal pressurization** increases temperature → raises pore pressure → weakens the fault.  

   These processes compete, producing a fundamental stability trade-off in fault mechanics.