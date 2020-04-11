"""

A can repeat
B cannot repeat
both order matters
lengths m, n
write function that expects two lists
returns a sorted based on b
everything that's not in B, pushed to end of return value (sorted ascending)


which numbers in A are also in B? (and which arent)

"""


def amazing_sort(A, B):
    # [1, 2, 5, 5, 7, 8, 10]
    A_sorted = sorted(A)
    # [] + [2,5,5,10]
    res = []
    for n in B:
        if n in A:
            res.append(n)
        else:
    pass
