from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.bessel.bessel_class import BesselAttributes
from AsymmetryFactor.j1 import j1
import math


def test_j1_bessel():
    micro = 10**(-6)

    m = 1.57 - 0.038j
    x = 10
    ur = 1
    particle = ParticleAttributes(x, m, ur)

    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    angle = 10
    bessel_b = BesselAttributes(k, z0, angle)

    assert j1(particle, bessel_b)==-0.021566574845325228