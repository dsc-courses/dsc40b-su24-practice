def foo(numbers):
    """Assume that `numbers` is a list containing n numbers."""
    # counts is a Python dictionary, which is implemented using hash table
    counts = {}
    for x in numbers:
        for y in numbers:
            diff = abs(x - y)
            if diff not in counts:
                counts[diff] = 1
            else:
                counts[diff] = counts[diff] + 1
    return counts

foo([1, 2, 3, 4])
