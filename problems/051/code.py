def exists_pair_summing_to_max(arr):
    n = len(arr)
    maximum = max(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == maximum:
                return True
    return False
