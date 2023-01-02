import sys
sys.path.append('./')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from graphs.create_graph import plot_graphic
from timeit import default_timer as timer
import numpy as np

def j1_plane_wave_with_three_particles():
    ur = 1
    x = np.linspace(0.01, 20, 200)

    pw = BeamAttributes()

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j

    results_038 = []
    results_019 = []
    results_095 = []

    start = timer()
    for i in x:
        results_038.append(j1(ParticleAttributes(i, m_038, ur), pw))
        results_019.append(j1(ParticleAttributes(i, m_019, ur), pw))
        results_095.append(j1(ParticleAttributes(i, m_095, ur), pw))
    time = timer()-start

    print("time: ", time)

    results = [results_038, results_019, results_095]
    x_label = "Size Parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["M = 1.57 - i0.038", "M = 1.57 - i0.19", "M = 1.57 - i0.95"]

    plot_graphic(results, x, x_label, y_label, legend)
    

if __name__ == '__main__':
    j1_plane_wave_with_three_particles()
    