from AsymmetryFactor.beams.beam_class import BeamAttributes
from mpmath import exp
import scipy.special 
import scipy.integrate
import numpy as np
import math


class FrozenWaveAttributes(BeamAttributes):
    def __init__(self, k, z0, q, l, n_to_q, name="Frozen Wave Beam") -> None:
        super().__init__(name, k, z0)

        self.q = q
        self.l = l 
        self.n_to_q = n_to_q
        pass

    def print_frozen_wave_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("angle: ", self.angle)

    def gn(self, n):
        """
        TO DO: add description
        
        Parameters
        ----------
        n      :
        n_to_q :
        k      :
        z0     :
        l      :  
        q      :
        """
        i = 1j

        q_values = np.arange(self.n_to_q, (-self.n_to_q + 1))   
        result_sum = 0

        for q_i in q_values:
            kz_q = self.Kz_q(q_i)
            div_kz_q_k = kz_q / self.k

            frist_term_sum = self.A_q(q_i) / (1 + div_kz_q_k)
            second_term_sum = self.pi_m_n(1, n, div_kz_q_k) + self.tau_m_n(1, n, div_kz_q_k)
            third_term_sum = exp(i * kz_q * self.z0)
            
            result = frist_term_sum * second_term_sum * third_term_sum

            result_sum += result
                    
        return (-2)/(n*(n+1)) * result_sum


    def pi_m_n(self, m, n, x):
        """
        TO DO: add description
        
        Parameters
        ----------
        m :
        n :
        x :  
        """
        num = scipy.special.lpmn(m, n, x)[0][m][n]
        den = math.sqrt(1 - (x**2))
        
        return num/den


    def tau_m_n(self, m, n, x):
        """
        TO DO: add description
        
        Parameters
        ----------
        m :
        n :
        x :  
        """
        pmn = scipy.special.lpmn(m, n, x)[0][m][n]
        pmn1 = scipy.special.lpmn(m, n+1, x)[0][m][n+1]

        frist_term = -(n + 1) * x * pmn
        second_term = (n - m + 1) * pmn1

        num = frist_term + second_term
        den = math.sqrt(1 - (x**2))

        return num/den


    def Kz_q(self, q_i):
        """
        TO DO: add description
        
        Parameters
        ----------  
        q_i :
        L   :
        q   :
        """
        return self.q + ((2 * math.pi * q_i) / self.l)


    def A_q(self, q_i):
        """
        TO DO: add description
        
        Parameters
        ----------  
        l :
        q :
        """

        i = 1j

        pi = math.pi
        
        inferior_limit = self.l/12
        upper_limit = (11*self.l)/12

        frist_term = 1/self.l    
        common = (2 * pi * q_i)/self.l
        
        fun_cos = lambda iz: exp(-5 * (((iz - (0.5 * self.l)) ** 2)/(self.l**2))) * math.cos(((6 * math.pi * iz) / self.l)) * math.cos(common * iz)
        fun_sen = lambda iz: exp(-5 * (((iz - (0.5 * self.l)) ** 2)/(self.l**2))) * math.cos(((6 * math.pi * iz) / self.l)) * math.sin(common * iz)
        
        integral_cos = scipy.integrate.quad(fun_cos, inferior_limit, upper_limit, epsrel = 1e-19)[0]
        integral_sin = scipy.integrate.quad(fun_sen, inferior_limit, upper_limit, epsrel = 1e-15)[0]
            
        integrate_result = integral_cos + i*integral_sin
        
        return frist_term * integrate_result
        