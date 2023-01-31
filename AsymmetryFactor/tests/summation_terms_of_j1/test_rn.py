from AsymmetryFactor.summation_terms_of_j1.rn import term_r_n


def test_term_r_n():
    m = 1.57 - 0.038j
    x = [1, 10]
    n = 1
    
    assert term_r_n(m, x[0], n) == 0.09469112901748901 and term_r_n(m, x[1], n) == 5.486746301700906
