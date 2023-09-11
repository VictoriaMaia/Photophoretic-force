from AsymmetryFactor.particle import ParticleAttributes
from AsymmetryFactor.beams import PlaneWaveAttributes
from AsymmetryFactor.j1 import j1


def test_j1_plane_wave():
    # Test using plane wave
    m = 1.57 - 0.038j
    x = 10
    ur = 1
    
    particle = ParticleAttributes(x, m, ur)
    pw = PlaneWaveAttributes(name="Plane Wave")

    assert j1(particle, pw)==0.054413290391591596

