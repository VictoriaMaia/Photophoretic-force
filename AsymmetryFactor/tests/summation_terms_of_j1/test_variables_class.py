from AsymmetryFactor.summation_terms_of_j1.variables_class import compute_variables
from AsymmetryFactor.particle.particle_class import ParticleAttributes


def test_summation_variables():
    ur = 1
    m = 1.57 - 0.038j
    x = 0.01
    i = 1
    
    p = ParticleAttributes(x, m, ur)

    result = compute_variables(p, i)

    assert result.cn == 0.6716724532989616+0.01795366893557229j \
           and result.conj_cn ==  0.6716724532989616-0.01795366893557229j \
           and result.cn1 == 0.4008748717367793+0.021786481363911387j \
           and result.conj_cn1 == 0.4008748717367793-0.021786481363911387j \
           and result.dn == 1.0000243918345717-1.9887776031473516e-06j \
           and result.conj_dn == 1.0000243918345717+1.9887776031473516e-06j \
           and result.dn1 == 0.6365790911267893+0.015406886773684299j \
           and result.rn == 1.3516974801576655e-11 \
           and result.rn1 == 9.52507726212478e-17 \
           and result.sn == 1.7208691554172406e-11+4.165307770001008e-13j
