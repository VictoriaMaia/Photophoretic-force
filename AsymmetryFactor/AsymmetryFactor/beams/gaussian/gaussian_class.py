from AsymmetryFactor.beams.beam_class import BeamAttributes
from mpmath import exp


class GaussAttributes(BeamAttributes):
    def __init__(self, k, z0, s, name="Gaussian Beam") -> None:
        super().__init__(name, k, z0)
        self.s = s
        pass

    def print_gauss_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("s: ", self.s)

    def gn(self, n):
        """
        Calculates the beam shape coefficient of gaussian beam

        Parameters
        ----------
        n     : the current index of the summation of j1
        """
        i = 1j

        q = self.var_q()

        arg_1 = self.s**2
        arg_2 = ((n+(1/2))**2)
        arg_exp = -q*arg_1*arg_2
        result_exp = exp(arg_exp)

        arg_e = i * self.k * self.z0
        result_e = exp(arg_e)

        return q * result_exp * result_e

    def var_q(self):
        """
        Calculates the variable Q value
        """
        i = 1j
        second_term_sub = i * 2 * self.z0 * (self.s**2) * self.k

        return 1 / (1 + second_term_sub)
