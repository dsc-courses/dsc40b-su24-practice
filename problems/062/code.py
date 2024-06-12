import math

def iterative_binary_search(arr, target):

    start = 0
    stop = len(arr)

    while (stop - start) > 0:
        print(arr[start])
        middle = math.floor((start + stop) / 2)
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            stop = middle
        else:
            start = middle + 1

    return None
