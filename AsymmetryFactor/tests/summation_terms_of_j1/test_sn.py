from AsymmetryFactor.summation_terms_of_j1.sn import term_s_n


def test_term_s_n():
    m = 1.57 - 0.038j
    x = 20
    n = 1
    
    assert term_s_n(m, x, n) == 3.2001770186275906+126.32100411676237j
