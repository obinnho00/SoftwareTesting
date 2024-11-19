

def bubble_sort(arr):
    """Sorts a list using the Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped by the inner loop, the list is sorted
        if not swapped:
            break

    return arr



