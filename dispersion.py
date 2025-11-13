import numpy as np
from .structural_vacuum import c_eff

def omega_k(k, m, lambda_val, rho_v, kappa=1.0):
    """Relativistic-like dispersion: omega^2 = c_eff^2 k^2 + m^2."""
    ce = c_eff(lambda_val, rho_v, kappa)
    return np.sqrt(ce**2 * k**2 + m**2)

def schrodinger_epsilon(k, m, hbar=1.0):
    """Nonrelativistic limit: epsilon = hbar^2 k^2 / (2m)."""
    return hbar**2 * k**2 / (2.0 * m)
