from asymmetryFactorJ1.mathFunctions import mathFuncs as rb


def var_d_n(u_r, m, ka, n):
    chi_ka = rb.ricattiBessel_hn(n, ka)
    chi_d_ka = rb.ricattiBessel_hn_derivative(n, ka)
    psi_ka = rb.ricattiBessel_jn(n, ka)
    psi_m_ka = rb.ricattiBessel_jn(n, (m*ka))
    psi_d_ka = rb.ricattiBessel_jn_derivative(n, ka)
    psi_d_m_ka = rb.ricattiBessel_jn_derivative(n, (m*ka))
    
    num = m * m * ((chi_ka * psi_d_ka) - (chi_d_ka * psi_ka))
    den = (m * chi_ka * psi_d_m_ka) - (u_r * chi_d_ka * psi_m_ka)
    
    return num/den
