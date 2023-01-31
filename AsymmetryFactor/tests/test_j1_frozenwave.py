from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1
import math


def test_j1_frozen_wave():
    micro = 10**(-6)
    nano = 10**(-9)

    m = 1.57 - 0.038j
    x = 3
    ur = 1
    particle = ParticleAttributes(x, m, ur)

    var_lambda = 1064 * nano
    k = (2*math.pi) / var_lambda
    q = 0.8*k
    l = 400*micro
    n = -75
    z0 = 0
    frozen_wave_b = FrozenWaveAttributes(k, z0, q, l, n)

    assert j1(particle, frozen_wave_b)==6.6315735215388598e-10