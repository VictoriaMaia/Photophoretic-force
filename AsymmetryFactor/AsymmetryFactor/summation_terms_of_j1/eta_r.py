def eta_r(m, u_r):
    """
    Calculates the value of eta_r (particle permittivity)
    
    Parameters
    ----------
    m   : index of refraction of the particle
    u_r : the real part of the particle permeability
    """
    epsilon = (m**2) / u_r
    div_ur_epsilon = u_r/epsilon
    return div_ur_epsilon ** (1/2)
