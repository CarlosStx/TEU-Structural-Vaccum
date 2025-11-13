# TEU – Numerical Experiments Overview

This Colab notebook performs a set of minimal numerical tests inspired by the
Theory of Empty Universe (TEU) in order to check the internal consistency of
the structural–vacuum model.

The experiments are:

---

### 1. Dispersion relation and wave propagation

- We implement a relativistic-like dispersion relation
  $$
  \omega^2(k) = c_{\text{eff}}^{\,2} k^2 + m^2 ,
  $$
  and plot $\omega(k)$ for a representative choice of parameters.

- We then propagate a 1D structural wave packet and compare the numerical
  propagation speed with the analytic value $c_{\text{eff}}$.

---

### 2. Structural particle energy as a function of size

- We assume a spherically symmetric structural profile $\rho(r)$ and compute
  the deformation energy
  $$
  E(R) = 4\pi \int_0^\infty \left[ \tfrac12 \lambda
  \bigl(\partial_r\rho\bigr)^2 + V(\rho)\right] r^2\,dr ,
  $$
  as a function of the characteristic radius $R$.

- The energy curve shows a stable minimum at
  $R_\star \approx 0.2,\quad m_\star \approx 2.32$,
  which we interpret as a **structural particle configuration**.

---

### 3. Mass vs. vacuum rigidity ($\lambda$)

- For fixed vacuum density $\rho_v$ we compute how the structural mass
  scales with vacuum rigidity.

- A clear scaling law is observed:
  $$
  m(\lambda) \sim \lambda^\alpha,
  \qquad \alpha \approx 0.20 ,
  $$
  consistent with a stiffer vacuum storing more deformation energy.

---

### 4. Slow variation of the effective gravitational constant

- Using a simple relaxation model for the structural vacuum, TEU predicts
  a secular drift of the effective gravitational constant
  $$
  \frac{\dot G_{\text{eff}}}{G_{\text{eff}}}
  \approx 10^{-13}\ \text{yr}^{-1} ,
  $$
  which is compatible with the strongest current experimental bounds.

---

### 5. Numerical robustness

- We perform a convergence test of the radial energy integral, showing that
  $E(R)$ stabilizes as the number of grid points $N$ increases.

- The 1D wave-propagation test also confirms that the numerical wave speed
  matches the analytic value $c_{\text{eff}}$ with sub-percent relative error.

Together, these experiments provide a first numerical check that the TEU
structural–vacuum framework is mathematically consistent and produces the
expected qualitative behaviour: elastic-like waves, stable localized
configurations (particles), sensible scaling with vacuum rigidity and a very
small but potentially measurable variation of $G_{\text{eff}}$.
