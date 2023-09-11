from AsymmetryFactor.summation_terms_of_j1 import SummationVariables
from AsymmetryFactor.particle import ParticleAttributes


def test_summation_variables():
    ur = 1
    m = 1.57 - 0.038j
    x = 0.01
    i = 1
    
    p = ParticleAttributes(x, m, ur)

    result = SummationVariables(p, i)

    assert result.cn == 0.6716724532989616+0.01795366893557229j 
    assert result.conj_cn ==  0.6716724532989616-0.01795366893557229j
    assert result.cn1 == 0.4008748717367793+0.021786481363911387j
    assert result.conj_cn1 == 0.4008748717367793-0.021786481363911387j
    assert result.dn == 1.0000243918345717-1.9887776031473516e-06j
    assert result.conj_dn == 1.0000243918345717+1.9887776031473516e-06j
    assert result.dn1 == 0.6365790911267893+0.015406886773684299j
    assert result.rn == 1.3516974801576655e-11
    assert result.rn1 == 9.52507726212478e-17
    assert result.sn == 1.7208691554172406e-11+4.165307770001008e-13j
