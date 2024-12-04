def sort_array(arr):
    return sorted(arr)

def test_mr_add_constant():
    arr = [3, 1, 2]
    sorted_arr = sort_array(arr)
    
    arr_plus_const = [x + 5 for x in arr]
    sorted_arr_plus_const = sort_array(arr_plus_const)
    
    assert sorted_arr == [x - 5 for x in sorted_arr_plus_const]

def test_mr_already_sorted():
    arr = [1, 2, 3]
    sorted_arr = sort_array(arr)
    
    assert sorted_arr == arr

def test_mr_reverse_sort():
    arr = [1, 2, 3]
    reversed_arr = list(reversed(arr))
    sorted_again = sort_array(reversed_arr)
    
    assert sorted_again == arr

if __name__ == "__main__":
    test_mr_add_constant()
    test_mr_already_sorted()
    test_mr_reverse_sort()
    print("All metamorphic tests passed for sort_array function.")
