# -------------------------------------------------
# Question 2: Determine whether the mutant is killed or alive.
# -------------------------------------------------

# Original Program
import math

def is_perfect_square(number):
    """Check if a given number is a perfect square."""
    if number < 0:
        return False  # Negative numbers can't be perfect squares
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number  # True if square of sqrt equals the number

# Mutated Program
def mutated_is_perfect_square(number):
    """Mutated Perfect Square Checker."""
    if number < 0:
        return False
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt != number  # Mutated line: Changed == to !=

# Test Cases
def test_is_perfect_square():
    # Test cases for the original program
    assert is_perfect_square(25) == True  # 5*5 = 25
    assert is_perfect_square(16) == True  # 4*4 = 16
    assert is_perfect_square(20) == False  # Not a perfect square
    assert is_perfect_square(-4) == False  # Negative number

def test_mutated_is_perfect_square():
    # Test cases for the mutant program
    assert mutated_is_perfect_square(25) == True  # Mutant returns False
    assert mutated_is_perfect_square(16) == True  # Mutant returns False
    assert mutated_is_perfect_square(20) == False
    assert mutated_is_perfect_square(-4) == False

# Main Execution
if __name__ == "__main__":
    print("Testing Original Program:")
    test_is_perfect_square()
    print("All tests for the original program passed!")

    print("\nTesting Mutated Program:")
    try:
        test_mutated_is_perfect_square()
        print("All tests for the mutant program passed!")
    except AssertionError as e:
        print("Test failed for the mutated program:", e)

# Analysis of Test Results
"""
Test Case Analysis:
1. Test Case: 25
   - Expected: True (Perfect square, 5*5=25)
   - Original: True
   - Mutant: False
   - Result: Mutant **killed**

2. Test Case: 16
   - Expected: True (Perfect square, 4*4=16)
   - Original: True
   - Mutant: False
   - Result: Mutant **killed**

3. Test Case: 20
   - Expected: False (Not a perfect square)
   - Original: False
   - Mutant: False
   - Result: Mutant **alive**

4. Test Case: -4
   - Expected: False (Negative numbers are not perfect squares)
   - Original: False
   - Mutant: False
   - Result: Mutant **alive**

Mutation Score Calculation:
- Killed Mutants: 2
- Total Mutants: 4
- Mutation Score: (2 / 4) = 0.5 or 50%.

"""