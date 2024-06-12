import math
def binary_search(arr, t, start, stop):
    if stop - start <= 0:
        return None
    middle = math.floor((start + stop)/2)
    print(arr[middle]) # <---- this line is new
    if arr[middle] == t:
        return middle
    elif arr[middle] > t:
        return binary_search(arr, t, start, middle)
    else:
        return binary_search(arr, t, middle+1, stop)
