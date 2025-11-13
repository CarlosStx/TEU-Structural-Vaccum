import numpy as np
from src.teu.structural_vacuum import c_eff
from src.teu.dispersion import omega_k, schrodinger_epsilon

def test_c_eff_positive():
    ce = c_eff(lambda_val=1.0, rho_v=1.0, kappa=1.0)
    assert ce > 0

def test_c_eff_scaling():
    ce1 = c_eff(lambda_val=1.0, rho_v=1.0, kappa=1.0)
    ce2 = c_eff(lambda_val=4.0, rho_v=1.0, kappa=1.0)
    assert np.isclose(ce2, 2.0 * ce1)

def test_dispersion_relations_limit():
    k = 0.01
    m = 1.0
    lam = 1.0
    rho_v = 1.0
    om = omega_k(k, m, lam, rho_v)
    eps = schrodinger_epsilon(k, m)
    assert om > m
    assert eps > 0
