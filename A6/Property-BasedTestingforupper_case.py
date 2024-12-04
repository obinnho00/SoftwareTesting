from hypothesis import given
import hypothesis.strategies as st

def to_upper_case(input_str):
    if input_str is None:
        raise ValueError("Input string cannot be None")
    return input_str.upper()

# Handle non-alphabetic characters properly.
@given(st.text())
def test_upper_case(input_str):
    output_str = to_upper_case(input_str)
    
    # Check that all alphabetic characters are uppercase, and non-alphabetic characters are unchanged
    assert all(
        c.isupper() if c.isalpha() else True
        for c in output_str
    )


@given(st.text(min_size=1, max_size=10).filter(lambda x: x.islower()))
def test_upper_case_conversion(input_str):
    assert to_upper_case(input_str) == input_str.upper()


@given(st.text(min_size=1, max_size=10).filter(lambda x: x.isupper()))
def test_upper_case_no_change(input_str):
    assert to_upper_case(input_str) == input_str

if __name__ == "__main__":
    test_upper_case()
    test_upper_case_conversion()
    test_upper_case_no_change()
    print("All tests passed for to_upper_case function.")
