from .mathFunctions.ricattiBesselFunctions import ricattiBessel as rb

def varC_n (u_r, M, ka, n):
    chi_ka = rb.ricattiBessel_hn(n, ka)
    chiD_ka = rb.ricattiBessel_hn_derivative(n, ka)
    psi_ka = rb.ricattiBessel_jn(n, ka)
    psi_Mka = rb.ricattiBessel_jn(n, (M*ka))
    psiD_ka = rb.ricattiBessel_jn_derivative(n, ka)
    psiD_Mka = rb.ricattiBessel_jn_derivative(n, (M*ka))
    
    num = M * u_r * ((chi_ka * psiD_ka) - (chiD_ka * psi_ka))
    den = (u_r * chi_ka * psiD_Mka) - (M * chiD_ka * psi_Mka)
    
    return num/den
