import math

def modified_binary_search(arr, t, start, stop, last_seen=None):
    if stop - start <= 0:
        return last_seen

    middle = math.floor((start + stop) / 2)

    if arr[middle] == t:
        return modified_binary_search(arr, t, start, middle, last_seen=middle)
    elif arr[middle] > t:
        return modified_binary_search(arr, t, start, middle, last_seen=last_seen)
    else:
        return modified_binary_search(arr, t, middle+1, stop, last_seen=last_seen)
