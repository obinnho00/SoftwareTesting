from hypothesis import given, assume
import hypothesis.strategies as st
import math

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@given(st.integers(min_value=0, max_value=20))
def test_factorial_positive(n):
    
    assert factorial(n) > 0

@given(st.integers(min_value=0, max_value=20))
def test_factorial_zero(n):
    
    if n == 0:
        assert factorial(n) == 1

@given(st.integers(min_value=1, max_value=20))
def test_factorial_recursive_property(n):
    
    assert factorial(n) == n * factorial(n - 1)

if __name__ == "__main__":
    test_factorial_positive()
    test_factorial_zero()
    test_factorial_recursive_property()
    print("All tests passed for factorial function.")
