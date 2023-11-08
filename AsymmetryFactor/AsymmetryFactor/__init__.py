"""

Asymmetry factor for structural beams

asymmetry factor is a package to calculate and simulate the asymmetry factor
given the information about the particle and the beam used.

The implemented beams that can currently be used are:

Plane wave beam
Gaussian beam
Bessel beam
Frozen wave beam
"""

from AsymmetryFactor import summation_terms_of_j1
from . import j1

__all__ = ('summation_terms_of_j1', 'j1')
