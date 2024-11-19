import pytest
from bubble_sort import bubble_sort

def test_bubble_sort():
    # General test cases
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([]) == []  # Empty list
    assert bubble_sort([1]) == [1]  # Single element
    assert bubble_sort([2, 1]) == [1, 2]  # Two elements
    assert bubble_sort([3, 3, 3]) == [3, 3, 3]  # All elements are the same

    # Edge cases
    assert bubble_sort([5, -1, 0, 3, -4]) == [-4, -1, 0, 3, 5]  # Mixed positive and negative numbers
    assert bubble_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]  # Reverse sorted
    assert bubble_sort([-1, -3, -2]) == [-3, -2, -1]  # Negative numbers
    assert bubble_sort([0, 0, 0, 0]) == [0, 0, 0, 0]  # All zeros
