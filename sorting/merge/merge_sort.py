def merge_sort(arr):
    """
    Sorts an array in ascending order using the Merge Sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The function sorts the input array in place.
    """
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

def merge(left, right, arr):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (list): The left half of the array to be merged.
        right (list): The right half of the array to be merged.
        arr (list): The array in which the merged result will be stored.

    Returns:
        None: The function modifies the input array in place by merging the left and right halves.
    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)