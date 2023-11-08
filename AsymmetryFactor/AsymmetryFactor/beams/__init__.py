"""

This subpackage has the definitions of the beams used as a child class to class
BeamAttributes containing its implementations of the term gn (Beam Shape Coefficients)
and necessary auxiliary functions.

To add another beam, just create a child class and add the necessary functions.

"""

from .planewave.plane_wave_class import PlaneWaveAttributes
from .gaussian.gaussian_class import GaussAttributes
from .bessel.bessel_class import BesselAttributes
from .frozenwave.frozenwave_class import FrozenWaveAttributes
from .beam_class import BeamAttributes

__all__ = ('PlaneWaveAttributes', 'GaussAttributes',
           'BesselAttributes', 'FrozenWaveAttributes',
           'BeamAttributes')
