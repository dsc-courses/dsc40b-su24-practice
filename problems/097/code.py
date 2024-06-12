def intersection(A, B):
    common = set()
    for x in A:
        if x in B:
            common.add(x)
    return common
