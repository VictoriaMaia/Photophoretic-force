from AsymmetryFactor.beams.beam_class import BeamAttributes
from mpmath import exp
import scipy.special
import scipy.integrate
import numpy as np
import math


class FrozenWaveAttributes(BeamAttributes):
    def __init__(self, k, z0, q, L, n_to_q, name="Frozen Wave Beam") -> None:
        super().__init__(name, k, z0)

        self.q = q
        self.L = L
        self.n_to_q = n_to_q
        pass

    def print_frozen_wave_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("angle: ", self.angle)

    def gn(self, n):
        """
        Calculates the Beam Shape Coefficients (gn) of the Frozen Wave beam

        Parameters
        ----------
        n  : the current index of the summation of j1
        """
        i = 1j

        q_values = np.arange(self.n_to_q, (-self.n_to_q + 1))
        result_sum = 0

        for q_i in q_values:
            kz_q = self.Kz_q(q_i)
            div_kz_q_k = kz_q / self.k

            frist_term_sum = self.A_q(q_i) / (1 + div_kz_q_k)
            second_term_sum = self.pi_m_n(1, n, div_kz_q_k) + \
                self.tau_m_n(1, n, div_kz_q_k)
            third_term_sum = exp(i * kz_q * self.z0)

            result = frist_term_sum * second_term_sum * third_term_sum

            result_sum += result

        return (-2) / (n * (n + 1)) * result_sum

    def pi_m_n(self, m, n, x):
        """
        Calculate the value of the function Pi, a generalized Legendre function

        Parameters
        ----------
        m and n : are inputs of Legendre functions of the first kind (lpmn)
        x       : size of the particle 
        """
        num = scipy.special.lpmn(m, n, x)[0][m][n]
        den = math.sqrt(1 - (x**2))

        return num / den

    def tau_m_n(self, m, n, x):
        """
        Calculate the value of the function Tau, a generalized Legendre function

        Parameters
        ----------
        m and n : are inputs of Legendre functions of the first kind (lpmn)
        x       : size of the particle 
        """
        pmn = scipy.special.lpmn(m, n, x)[0][m][n]
        pmn1 = scipy.special.lpmn(m, n + 1, x)[0][m][n + 1]

        frist_term = -(n + 1) * x * pmn
        second_term = (n - m + 1) * pmn1

        num = frist_term + second_term
        den = math.sqrt(1 - (x**2))

        return num / den

    def Kz_q(self, q_i):
        """
        Calculates the longitudinal wavenumber of the q_ith bessel beam.

        In the text of the thesis this variable is called Beta_q.

        Parameters
        ----------
        q_i : the current index of the summation of gn
        """
        return self.q + ((2 * math.pi * q_i) / self.L)

    def A_q(self, q_i):
        """
        Calculates the q_ith complex amplitude that weights the q_ith Bessel beam that makes up the FW

        Parameters
        ----------
        q_i : the current index of the summation of gn
        """

        i = 1j

        pi = math.pi

        inferior_limit = self.L / 12
        upper_limit = (11 * self.L) / 12

        frist_term = 1 / self.L
        common = (2 * pi * q_i) / self.L

        fun_cos = lambda iz: \
            exp(-5 * (((iz - (0.5 * self.L)) ** 2) / (self.L ** 2))) * \
            math.cos(((6 * math.pi * iz) / self.L)) * \
            math.cos(common * iz)  # noqa: E731

        fun_sen = lambda iz: \
            exp(-5 * (((iz - (0.5 * self.L)) ** 2) / (self.L ** 2))) * \
            math.cos(((6 * math.pi * iz) / self.L)) * \
            math.sin(common * iz)  # noqa: E731

        integral_cos = scipy.integrate.quad(fun_cos,
                                            inferior_limit, upper_limit,
                                            epsrel=1e-19)[0]

        integral_sin = scipy.integrate.quad(fun_sen,
                                            inferior_limit, upper_limit,
                                            epsrel=1e-15)[0]

        integrate_result = integral_cos + i * integral_sin

        return frist_term * integrate_result
