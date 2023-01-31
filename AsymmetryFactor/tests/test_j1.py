from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1


def test_j1():
    # Test using plane wave
    m = 1.57 - 0.038j
    x = 10
    ur = 1
    
    particle = ParticleAttributes(x, m, ur)
    pw = BeamAttributes()

    assert j1(particle, pw)==0.054413290391591596
