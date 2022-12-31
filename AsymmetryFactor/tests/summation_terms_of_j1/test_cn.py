from AsymmetryFactor.summation_terms_of_j1.cn import term_c_n


def test_term_c_n():
    m = 1.57 - 0.038j
    u_r = 1
    x = 20 
    n = 1
    
    assert term_c_n(u_r, m, x, n) == 0.20833911004916092+0.5042975427280426j 
