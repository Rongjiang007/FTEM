Framework
===========

To solve the earthquake dynamic simulation problem using boundary integral equations, 
we assume the fault plane is embedded in an elastic half-space or full-space with 
homogeneous and constant elastic moduli. A constant tectonic loading rate is imposed 
across the entire fault interface. The elastic stress transfer due to slip on the fault 
is described in Equations (1) (shear stress) and (2) (normal stress), with the radiation 
damping assumption :cite:p:`rice1993spatio`.

.. math::
   :label: forcebalance

   \tau_{i} = \tau_{0} - \sum_{j=1}^{n} k_{ij}^s \left( u_{j} - V_{pl} t \right) - \frac{\mu}{2c_s} \frac{\partial u_{i}}{\partial t}

.. math::
   :label: normalstressbalance

   \bar{\sigma}_{i} = \bar{\sigma}_{0} + \sum_{j=1}^{n} k_{ij}^N \left(u_{j} - V_{pl} t\right)
   
   
where :math:`V_{pl}` is the imposed tectonic slip rate, :math:`\mu` is the shear modulus, 
:math:`c_s` is the shear wave speed, and :math:`u_j` is the slip at the :math:`j`-th element. 
The kernels :math:`k_{ij}^s` and :math:`k_{ij}^N` represent the shear and normal stiffness 
matrices, respectively. The last term in Equation :eq:`forcebalance` captures radiation damping 
and approximates inertial effects, adopted to avoid unbounded slip velocity that would otherwise 
develop in quasi-static models.

To compute :math:`k_{ij}^s` and :math:`k_{ij}^N`, analytical formulas for static stress induced 
by triangular dislocations in a homogeneous elastic full-space and half-space are employed 
:cite:`nikkhoo2015triangular`. Since the goal is to simulate three-dimensional complex non-planar 
fault geometries, optimizations specific to planar faults (e.g. Fourier-domain construction) 
are not applicable. Instead, CPU-based multiprocessing or MPI are used 
to accelerate the computation of Green's functions.

---

Time-Differentiated Formulation
-------------------------------

By differentiating Equations :eq:`forcebalance` and :eq:`normalstressbalance`, and considering 
external loading, we obtain:

.. math::
   \frac{d\tau_{i}}{dt} = -\sum_{j=1}^{N} k_{ij}^s \left(V_{j} - V_{pl}\right) + \dot{\tau}_{i} - \frac{\mu}{2c_s} \frac{dV_{i}}{dt}
   :label: VKs

.. math::
   \frac{d\sigma_{i}}{dt} = \sum_{j=1}^{N} k_{ij}^N V_{j} + \dot{\sigma}_{i}
   :label: VKn

where :math:`\dot{\tau}_i` and :math:`\dot{\sigma}_i` are tectonic loading rates.

---

Friction Law
------------

To close the system, we apply the laboratory-derived rate-and-state friction (RSF) law 
:cite:`dieterich1979modeling_b,ruina1983slip`. The friction coefficient under the regularized 
aging law is:

.. math::
   f(V, \theta) = a \sinh^{-1} \left[ \frac{V}{2V_0} \exp\left(\frac{f_0 + b\ln\left(\frac{V_0 \theta}{d_c}\right)}{a}\right) \right]

.. math::
   \frac{d\theta}{dt} = 1 - \frac{V\theta}{d_c}

with :math:`d_c` the characteristic slip distance, :math:`V_0` the reference slip rate, 
:math:`f_0` the reference friction coefficient, and :math:`a`, :math:`b` the RSF parameters.

We define a transformed state variable:

.. math::
   \psi = f_0 + b \ln \left( \frac{V_0 \theta}{d_c} \right)

giving the transformed law:

.. math::
   \frac{\tau_i}{\sigma_i} = a \arcsin\left( \frac{V_i}{2V_0} \exp\left(\frac{\psi_i}{a}\right) \right)

.. math::
   \frac{d\psi_i}{dt} = \frac{b}{d_c} \left[ V_0 \exp\left( \frac{f_0 - \psi_i}{b} \right) - V_i \right]
   :label: dfaidt

---

System of Equations
-------------------

By substitution, Equations :eq:`VKs`, :eq:`VKn`, and :eq:`dfaidt` yield a coupled system of ODEs 
of dimension :math:`4N`:

.. math::
   \frac{dy}{dt} = f(y)

with:

.. math::
   y = (\psi_1, \dots, \psi_N, \tau_{1,1}, \dots, \tau_{1,N}, \tau_{2,1}, \dots, \tau_{2,N}, \sigma_1, \dots, \sigma_N)

This system is solved using the Dormand–Prince 5th-order Runge–Kutta method with adaptive 
time stepping :cite:`press2007numerical`.

---

Hierarchical Matrix Compression and MPI
---------------------------------------

Following Börm :cite:`borm2003introduction`, **PyQuake3D** implements H-matrix compression in 
``Hmatrix.py`` with MPI-based parallel acceleration. The H-matrix framework decomposes stiffness 
matrices into low-rank far-field blocks and dense near-field blocks, organized into cluster and 
block trees.

Cluster tree construction is based on geometric splitting, while block trees pair clusters to 
determine admissibility for low-rank approximation. This design enables efficient compression 
and distributed memory scalability.

---

References
----------

.. bibliography::
   :style: unsrt
   :filter: docname in docnames

