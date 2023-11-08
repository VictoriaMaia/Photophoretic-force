from AsymmetryFactor.beams.beam_class import BeamAttributes
from mpmath import exp
import scipy.special
import math


class BesselAttributes(BeamAttributes):
    def __init__(self, k, z0, angle, name="Bessel Beam") -> None:
        super().__init__(name, k, z0)
        self.angle = angle
        pass

    def print_bessel_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("angle: ", self.angle)

    def gn(self, n):
        """
        Calculates the Beam Shape Coefficients (gn) of the Bessel beam

        Parameters
        ----------
        n  : the current index of the summation of j1
        """
        i = 1j

        cos_angle = math.cos(math.radians(self.angle))

        tau_1_n = self.tau_m_n(1, n, cos_angle)
        pi_1_n = self.pi_m_n(1, n)

        frist_term = - (1 / (n * (n + 1)))

        second_term = (tau_1_n/cos_angle) + pi_1_n

        arg_e = i * self.k * cos_angle * self.z0
        thir_term = exp(arg_e)

        return frist_term * second_term * thir_term

    def tau_m_n(self, m, n, x):
        """
        Calculate the value of the function Tau, a generalized Legendre function

        Parameters
        ----------
        m and n : are inputs of Legendre functions of the first kind (lpmn)
        x       : size of the particle 
        """
        pmn = scipy.special.lpmn(m, n, x)[0][m][n]
        pmn1 = scipy.special.lpmn(m, n+1, x)[0][m][n+1]

        frist_term = -(n + 1) * x * pmn
        second_term = (n - m + 1) * pmn1

        num = frist_term + second_term

        if x == 1:
            den = math.sqrt(1 - 0.999999999)
        else:
            den = math.sqrt(1 - (x**2))

        return num/den

    def pi_m_n(self, m, n):
        """
        Calculate the value of the function Pi, a generalized Legendre function

        Parameters
        ----------
        m and n : are inputs of Legendre functions of the first kind (lpmn)
        """
        cos_alpha = math.cos(math.radians(self.angle))
        num = scipy.special.lpmn(m, n, cos_alpha)[0][m][n]

        sin_alpha = math.sin(math.radians(self.angle))

        return num/sin_alpha
