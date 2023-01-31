def epsilon_imag(m, u_r):
    """
    Calculates the value of imaginary part of epsilon value.
    TO DO: what is epsilon?
    
    Parameters
    ----------
    m   : index of refraction of the particle
    u_r : the real part of the particle permeability
    """
    epsilon = (m**2) / u_r
    return - epsilon.imag
