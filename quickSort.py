def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        pi = partition(arr, low, high)
        # Recursively sort left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high] # choose last element as pivot
    i = low - 1 # index of smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap
    # Put pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
# Example
arr = [29, 10, 14, 37, 13]
print("Original:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted :", arr)