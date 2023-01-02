from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.gaussian.gaussian_class import GaussAttributes
from AsymmetryFactor.j1 import j1
import math


def test_j1_gaussian():
    micro = 10**(-6)

    m = 1.57 - 0.038j
    x = 10
    ur = 1
    particle = ParticleAttributes(x, m, ur)

    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    s = 0.1
    gauss_b = GaussAttributes(k, z0, s)

    assert j1(particle, gauss_b)==-0.017788439680167058