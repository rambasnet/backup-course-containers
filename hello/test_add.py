from pytest import approx
from add import add

def test_add_ints():
    assert add(1,2) == 3
    assert add(1,-1) == 0

    # Python can represent large integers exactly if they fit in memory.
    # Many languages use a fixed-size representations which leads to
    # overflow (but runs much faster, which is the trade-off).
    #
    # Do not expect this to be correct in C or C++!
    #
    assert add(10**40,1) == 10000000000000000000000000000000000000001

def test_add_floats():
    # Python approximates fractions/floats in base 2 exponential
    # notation with 54 digits in the mantessa and a power of 2 exponent
    #  x ≈ ±1.011...(50 more binary digits) x 2^exponent
    # so floating point calculations are close but usually not exact.
    
    # 0.8333333333333334 != 0.8333333333333333
    assert 1-1/6 != add(1/3,1/2)

    # But it is close (approx can specify a relative or absolute error).
    # https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-approx
    assert approx(1-1/6,rel=1e-12) == add(1/3,1/2)
