# -------------------------------------------------
# Question 1: Leap Year Checker
# Write a program to check if a given year is a leap year.
# Then, analyze the program with a mutant that changes the logic for divisibility by 400.
# Provide test cases to verify the original and mutant programs and calculate the mutation score.
# -------------------------------------------------

# Original Leap Year Checker Program
class LeapYearChecker:
    @staticmethod
    def is_leap_year(year):
        """Check if a given year is a leap year."""
        if year % 4 != 0:
            return False  # Not divisible by 4, so not a leap year
        elif year % 100 != 0:
            return True  # Divisible by 4 but not 100, so a leap year
        elif year % 400 != 0:
            return False  # Divisible by 100 but not 400, so not a leap year
        else:
            return True  # Divisible by both 100 and 400, so a leap year

# Mutated Leap Year Checker Program
class MutatedLeapYearChecker:
    @staticmethod
    def is_leap_year(year):
        """Mutant Leap Year Checker."""
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 == 0:  # Mutated line: Changed != to ==
            return False  # Incorrectly returns False for years divisible by 400
        else:
            return True

# Test Cases for Leap Year Checker
def test_is_leap_year():
    # Test cases for the original program
    assert LeapYearChecker.is_leap_year(2000) == True  # Divisible by 400
    assert LeapYearChecker.is_leap_year(1900) == False  # Divisible by 100 but not 400
    assert LeapYearChecker.is_leap_year(2004) == True  # Divisible by 4 but not 100
    assert LeapYearChecker.is_leap_year(2001) == False  # Not divisible by 4

def test_mutated_is_leap_year():
    # Test cases for the mutant program
    assert MutatedLeapYearChecker.is_leap_year(2000) == True  # Mutant returns False
    assert MutatedLeapYearChecker.is_leap_year(1900) == False
    assert MutatedLeapYearChecker.is_leap_year(2004) == True
    assert MutatedLeapYearChecker.is_leap_year(2001) == False

# Main execution
if __name__ == "__main__":
    print("Testing Original Program:")
    test_is_leap_year()
    print("All tests for the original program passed!")

    print("\nTesting Mutated Program:")
    try:
        test_mutated_is_leap_year()
        print("All tests for the mutant program passed!")
    except AssertionError as e:
        print("Test failed for the mutated program:", e)

# Answer Analysis
"""
Test Case Analysis:
1. Test Case: 2000
   - Expected: True (Leap year, divisible by 400)
   - Original: True
   - Mutant: False
   - Result: Mutant **killed**

2. Test Case: 1900
   - Expected: False (Divisible by 100 but not 400)
   - Original: False
   - Mutant: False
   - Result: Mutant **alive**

3. Test Case: 2004
   - Expected: True (Leap year, divisible by 4 but not 100)
   - Original: True
   - Mutant: True
   - Result: Mutant **alive**

4. Test Case: 2001
   - Expected: False (Not a leap year)
   - Original: False
   - Mutant: False
   - Result: Mutant **alive**

Mutation Score Calculation:
- Killed Mutants: 1 (for year 2000)
- Total Mutants: 4
- Mutation Score: (1 / 4) = 0.25 or 25%.

"""
