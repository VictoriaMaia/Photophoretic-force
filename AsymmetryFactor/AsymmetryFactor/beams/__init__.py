"""

This subpackage has the ...
TODO: add description!

"""

from .gaussian.gaussian_class import GaussAttributes
from .bessel.bessel_class import BesselAttributes
from .frozenwave.frozenwave_class import FrozenWaveAttributes

# TODO add class improvements
# from .gaussian.gn_functions import gn_gaussian_beam
from .bessel.gn_functions import gn_bessel_beam
from .frozenwave.gn_functions import gn_frozen_wave_beam, gn_frozen_wave_beam_with_parallel, gn_frozen_wave_beam_with_calculate_time
