from merge.merge_sort import merge_sort, merge

def test_merge_sort_empty():
    arr = []
    merge_sort(arr)
    assert arr == []

def test_merge_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_merge_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_merge_sort_mixed():
    arr = [3, 1, 4, 2, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]
