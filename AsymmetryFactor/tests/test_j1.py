from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.j1 import j1


def test_j1():
    # Test using plane wave
    m = 1.57 - 0.038j
    x = 10
    ur = 1
    
    particle = ParticleAttributes(x, m, ur)

    assert j1(particle)==0.054413290391591596
