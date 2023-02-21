from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.beams.gaussian.gn_functions import *

class GaussAttributes(BeamAttributes):
    def __init__(self, k, z0, s, name="Gaussian Beam") -> None:
        super().__init__(name)

        self.k = k
        self.z0 = z0
        self.s = s
        pass

    def print_beam_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("s: ", self.s)

    def gn_beam(self, n):
        """
        TODO: add description
        
        Parameters
        ----------
        
        """
        i = 1j
        
        q = var_q(self.z0, self.s, self.k)
        
        arg_1 = self.s**2
        arg_2 = ((n+(1/2))**2)
        arg_exp = -q*arg_1*arg_2
        result_exp = exp(arg_exp)

        arg_e = i*self.k * self.z0
        result_e = exp(arg_e)
        
        return q*result_exp*result_e