import numpy as np

def c_eff(lambda_val: float, rho_v: float, kappa: float = 1.0) -> float:
    """Effective propagation speed: c_eff^2 = lambda / (kappa * rho_v)."""
    if rho_v <= 0 or lambda_val <= 0:
        raise ValueError("lambda and rho_v must be positive.")
    return np.sqrt(lambda_val / (kappa * rho_v))
