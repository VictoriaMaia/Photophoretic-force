from AsymmetryFactor.summation_terms_of_j1.dn import term_d_n


def test_term_d_n():
    m = 1.57 - 0.038j
    u_r = 1
    x = 20 
    n = 1
    
    assert term_d_n(u_r, m, x, n) == 0.38847687295178984+0.8603497994156294j
