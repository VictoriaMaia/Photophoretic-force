from asymmetryFactorJ1.mathFunctions import mathFuncs as rb


def var_c_n(u_r, m, ka, n):
    chi_ka = rb.ricattiBessel_hn(n, ka)
    chi_derivative_ka = rb.ricattiBessel_hn_derivative(n, ka)
    psi_ka = rb.ricattiBessel_jn(n, ka)
    psi_m_ka = rb.ricattiBessel_jn(n, (m*ka))
    psi_derivative_ka = rb.ricattiBessel_jn_derivative(n, ka)
    psi_derivative_m_ka = rb.ricattiBessel_jn_derivative(n, (m*ka))
    
    num = m * u_r * ((chi_ka * psi_derivative_ka) - (chi_derivative_ka * psi_ka))
    den = (u_r * chi_ka * psi_derivative_m_ka) - (m * chi_derivative_ka * psi_m_ka)
    
    return num/den
