from typing import List, Iterable, Set, Callable, Optional, Union, Tuple
from timeit import timeit
from random import randint
from time import perf_counter


def geeks_for_geeks():
    # https://www.geeksforgeeks.org/find-union-and-intersection-of-two-unsorted-arrays/
    # Python3 program to find union and intersection
    # using similar Hashing Technique
    # without using any predefined Java Collections
    # Time Complexity best case & avg case = O(m+n)
    # Worst case = O(nlogn)

    # Prints intersection of arr1[0..n1-1] and
    # arr2[0..n2-1]

    def findPosition(a: List[int], b: List[int]) -> None:
        a_len = len(a)
        b_len = len(b)
        v = a_len + b_len
        ans = [0] * v
        zero1 = 0
        zero2 = 0
        print("Intersection :", end=" ")

        # Iterate first array
        for i in range(a_len):
            zero1 = iterateArray(a, v, ans, i)

            # Iterate second array
        for j in range(b_len):
            zero2 = iterateArray(b, v, ans, j)

        zero = zero1 + zero2
        placeZeros(v, ans, zero)
        printUnion(v, ans, zero)

    # Prints union of arr1[0..n1-1] and arr2[0..n2-1]
    def printUnion(v: int, ans: List[int], zero: int) -> None:
        zero1 = 0
        print("\nUnion :", end=" ")
        for i in range(v):
            if ((zero == 0 and ans[i] == 0) or
                    (ans[i] == 0 and zero1 > 0)):
                continue
            if ans[i] == 0:
                zero1 += 1
            print(ans[i], end=",")

    def placeZeros(v: int, ans: List[int], zero: int) -> None:
        if zero == 2:
            print("0")
            d = [0]
            placeValue(d, ans, 0, 0, v)
        if zero == 1:
            d = [0]
            placeValue(d, ans, 0, 0, v)

    def iterateArray(a: List[int], v: int, ans: List[int], i: int) -> int:
        if a[i] != 0:
            p = a[i] % v
            placeValue(a, ans, i, p, v)
        else:
            return 1

        return 0

    def placeValue(a: List[int], ans: List[int], i: int, p, v: int) -> None:
        p = p % v
        if ans[p] == 0:
            ans[p] = a[i]
        else:
            if ans[p] == a[i]:
                print(a[i], end=",")
            else:
                # Hashing collision happened increment
                # position and do recursive call
                p = p + 1
                placeValue(a, ans, i, p, v)

            # Driver code

    A = [7, 1, 5, 2, 3, 6]
    B = [3, 8, 6, 20, 7]
    print('A: ', A)
    print('B: ', B)
    findPosition(A, B)


def _dumb(a: Iterable[int], b: Iterable[int]) -> List[int]:
    intersection = []
    for x in a:
        for y in b:
            if x == y:
                intersection.append(x)
    return intersection


#     fn                                                type    sorted  type    sorted  dumb
# 1   dumb_sets                                         Set     F       Set     F       T
# 2   sets                                              Set     F       Set     F       F
# 3   dumb_presorted_sets                               Set     T       Set     ?       T
# 4   presorted_sets                                    Set     T       Set     ?       F
# 5   unsorted_lists                                    List    F       List    F
# 6   unsorted_lists_to_sorted_lists                    List    F       List    T
# 7   presorted_lists                                   List    T       List    ?
# 8   unsorted_lists_to_dumb_sets                       List    F       Set     F       T
# 9   unsorted_lists_to_set_a                           List    F       Set     F       F
# 10  unsorted_lists_to_set_both                        List    F       Set     F       F
# 11  unsorted_lists_to_sets_and_back                   List    F       Set->List/F
# 12  unsorted_lists_to_sets_and_sorted_lists           List    F       Set->List/T
# 13  unsorted_lists_to_sorted_lists_to_dumb_sets       List    F       List/T->Set     T
# 14  unsorted_lists_to_sorted_lists_to_sets            List    F       List/T->Set     F
# 15  presorted_lists_to_dumb_sets (8)                  List    T       Set     F       T
# 16  presorted_lists_to_set_a (9)                      List    T       Set     F       F
# 17  presorted_lists_to_set_both (10)                  List    T       Set     F       F
# 18  presorted_lists_to_sets_and_back (11)             List    T       Set->List/F
# 19  presorted_lists_to_sets_to_sorted_lists (12)      List    T       Set->List/T
# 20  unsorted_sets_to_lists                            Set     F       List    F
# 21  unsorted_sets_to_sorted_lists                     Set     F       List    T
# 22  presorted_sets_to_lists                           Set     T       List    ?
# 23  unsorted_sets_to_sorted_lists_to_dumb_sets        Set     F       List/T->Set    T
# 24  unsorted_sets_to_sorted_lists_to_sets             Set     F       List/T->Set    F
fn_to_num = dict(
    dumb_sets=1,
    sets=2,
    dumb_presorted_sets=3,
    presorted_sets=4,
    unsorted_lists=5,
    unsorted_lists_to_sorted_lists=6,
    presorted_lists=7,
    unsorted_lists_to_dumb_sets=8,
    unsorted_lists_to_set_a=9,
    unsorted_lists_to_set_both=10,
    unsorted_lists_to_sets_and_back=11,
    unsorted_lists_to_sets_and_sorted_lists=12,
    unsorted_lists_to_sorted_lists_to_dumb_sets=13,
    unsorted_lists_to_sorted_lists_to_sets=14,
    presorted_lists_to_dumb_sets=15,
    presorted_lists_to_set_a=16,
    presorted_lists_to_set_both=17,
    presorted_lists_to_sets_and_back=18,
    presorted_lists_to_sets_to_sorted_lists=19,
    unsorted_sets_to_lists=20,
    unsorted_sets_to_sorted_lists=21,
    presorted_sets_to_lists=22,
    unsorted_sets_to_sorted_lists_to_dumb_sets=23,
    unsorted_sets_to_sorted_lists_to_sets=24,
    )


# 3.5       1x
# 0.35      2x
# 0.035     3x
# 0.0035    4x
# 0.00035   5x
# 0.000035  6x

# 2
# A: 1M:100K, B: 10K:1K     0.00004~     //             6x
def sets(a: Set[int], b: Set[int]) -> Set[int]:
    return a.intersection(b)


# 4
# A: 1M:100K, B: 10K:1K     0.00005~       //            6x
def presorted_sets(a: Set[int], b: Set[int]) -> Set[int]:
    return a.intersection(b)


# 9
# A: 1M:100K, B: 10K:1K     0.005~          /             4x GOOD
def unsorted_lists_to_set_a(a: List[int], b: List[int]) -> Set[int]:
    return set(a).intersection(b)


# 10
# A: 1M:100K, B: 10K:1K     0.005~           /           4x
def unsorted_lists_to_set_both(a: List[int], b: List[int]) -> Set[int]:
    return set(a).intersection(set(b))


# 16
# A: 1M:100K, B: 10K:1K     0.01~         /          3x
def presorted_lists_to_set_a(a: List[int], b: List[int]) -> Set[int]:
    return set(a).intersection(b)


# 17
# A: 1M:100K, B: 10K:1K     0.01~          /         3x
def presorted_lists_to_set_both(a: List[int], b: List[int]) -> Set[int]:
    return set(a).intersection(set(b))


# 24
# A: 1M:100K, B: 10K:1K     0.02~         /      3x
def unsorted_sets_to_sorted_lists_to_sets(a: Set[int], b: Set[int]) -> Set[int]:
    return set(sorted(a)).intersection(sorted(b))


# 1
# A: 1M:100K, B: 10K:1K     3.5~                        1x
def dumb_sets(a: Set[int], b: Set[int]) -> List[int]:
    return _dumb(a, b)


# 3
# A: 1M:100K, B: 10K:1K     4~                         1x
def dumb_presorted_sets(a: Set[int], b: Set[int]) -> List[int]:
    return _dumb(a, b)


# 5
# A: 1M:100K, B: 10K:1K     2.8~                        1x
def unsorted_lists(a: List[int], b: List[int]) -> List[int]:
    return _dumb(a, b)


# 6
# A: 1M:100K, B: 10K:1K     2.4~                        1x
def unsorted_lists_to_sorted_lists(a: List[int], b: List[int]) -> List[int]:
    return _dumb(sorted(a), sorted(b))


# 7
# A: 1M:100K, B: 10K:1K     3~                          1x
def presorted_lists(a: List[int], b: List[int]) -> List[int]:
    return _dumb(a, b)


# 8
# A: 1M:100K, B: 10K:1K     3.2~                        1x
def unsorted_lists_to_dumb_sets(a: List[int], b: List[int]) -> List[int]:
    return _dumb(set(a), set(b))


# 11
# A: 1M:100K, B: 10K:1K     2.33~                       1x
def unsorted_lists_to_sets_and_back(a: List[int], b: List[int]) -> List[int]:
    return _dumb([*set(a)], [*set(b)])


# 12
# A: 1M:100K, B: 10K:1K     2.33~                       1x
def unsorted_lists_to_sets_and_sorted_lists(a: List[int], b: List[int]) -> List[int]:
    return _dumb(sorted(set(a)), sorted(set(b)))


# 13
# A: 1M:100K, B: 10K:1K     3.3~                        1x
def unsorted_lists_to_sorted_lists_to_sets(a: List[int], b: List[int]) -> List[int]:
    return _dumb(set(sorted(a)), set(sorted(b)))


# 14
# A: 1M:100K, B: 10K:1K     3.33~                       1x
def unsorted_lists_to_sorted_lists_to_dumb_sets(a: List[int], b: List[int]) -> List[int]:
    return _dumb(set(sorted(a)), set(sorted(b)))


# 15
# A: 1M:100K, B: 10K:1K     4~                      1x
def presorted_lists_to_dumb_sets(a: List[int], b: List[int]) -> List[int]:
    return _dumb(set(a), set(b))


# 18
# A: 1M:100K, B: 10K:1K     2.8~                    1x
def presorted_lists_to_sets_and_back(a: List[int], b: List[int]) -> List[int]:
    return _dumb([*set(a)], [*set(b)])


# 19
# A: 1M:100K, B: 10K:1K     2.8~                    1x
def presorted_lists_to_sets_to_sorted_lists(a: List[int], b: List[int]) -> List[int]:
    return _dumb(sorted(set(a)), sorted(set(b)))


# 20
# A: 1M:100K, B: 10K:1K     2.5~                1x
def unsorted_sets_to_lists(a: Set[int], b: Set[int]) -> List[int]:
    return _dumb([*a], [*b])


# 21
# A: 1M:100K, B: 10K:1K     2.5s~               1x
def unsorted_sets_to_sorted_lists(a: Set[int], b: Set[int]) -> List[int]:
    return _dumb(sorted(a), sorted(b))


# 22
# A: 1M:100K, B: 10K:1K     3~                  1x
def presorted_sets_to_lists(a: Set[int], b: Set[int]) -> List[int]:
    return _dumb([*a], [*b])


# 23
# A: 1M:100K, B: 10K:1K     3.3~                1x
def unsorted_sets_to_sorted_lists_to_dumb_sets(a: Set[int], b: Set[int]) -> List[int]:
    return _dumb(set(sorted(a)), set(sorted(b)))


ExpectsSets = Callable[[Set[int], Set[int]], Union[List[int], Set[int]]]
ExpectsLists = Callable[[List[int], List[int]], Union[List[int], Set[int]]]
MeasureFn = Union[ExpectsSets, ExpectsLists]


def measure(fn: MeasureFn,
            a_range: int, b_range: int,
            apply: ExpectsLists = None,
            iterations: int = 3) -> None:
    measures = []
    IterablesA = []
    IterablesB = []
    for _ in range(iterations):
        ListA = [randint(0, a_range * 10) for _ in range(a_range)]
        IterableA = apply(ListA) if apply is not None else ListA
        IterablesA.append(IterableA)
        ListB = [randint(0, b_range * 10) for _ in range(b_range)]
        IterableB = apply(ListB) if apply is not None else ListB
        IterablesB.append(IterableB)
    Iterables = zip(IterablesA, IterablesB)

    for IterableA, IterableB in Iterables:
        perf_start = perf_counter()
        res = fn(IterableA, IterableB)
        perf_end = perf_counter()
        measures.append(perf_end - perf_start)
    else:
        fn_name = fn.__name__
        fn_num = fn_to_num.get(fn_name)
        # print(f'{fn_name} (#{fn_num}) res: {res}')
        avg = sum(measures) / len(measures)
        zeroes = 1
        if 'e' in (avg_str := str(avg)):
            zeroes = int(avg_str[avg_str.index('e') + 2:]) + 1
        else:
            for c in avg_str.replace(".", ""):
                if c == '0':
                    zeroes += 1
                else:
                    break
        print(f'{fn_name} (#{fn_num}) avg: {avg}\t{zeroes}x', end='\n\n')


def everything(a_range: int, b_range: int):
    [measure(fn, a_range, b_range, set) for fn in (
        dumb_sets,
        sets,  # // 6x
        unsorted_sets_to_lists,
        unsorted_sets_to_sorted_lists,
        )]

    [measure(fn, a_range, b_range, lambda i: set(sorted(i))) for fn in (
        dumb_presorted_sets,
        presorted_sets,  # // 6x
        presorted_sets_to_lists,
        )]

    [measure(fn, a_range, b_range, sorted) for fn in (
        presorted_lists,
        presorted_lists_to_dumb_sets,
        presorted_lists_to_set_a,  # / 3x
        presorted_lists_to_set_both,  # / 3x
        presorted_lists_to_sets_and_back,
        presorted_lists_to_sets_to_sorted_lists,
        )]

    [measure(fn, a_range, b_range) for fn in (
        unsorted_lists,
        unsorted_lists_to_sorted_lists,
        unsorted_lists_to_dumb_sets,
        unsorted_lists_to_set_a,  # / 4x
        unsorted_lists_to_set_both,  # / 4x
        unsorted_lists_to_sets_and_back,
        unsorted_lists_to_sets_and_sorted_lists,
        unsorted_lists_to_sorted_lists_to_sets,
        unsorted_lists_to_sorted_lists_to_dumb_sets,

        unsorted_sets_to_sorted_lists_to_dumb_sets,
        unsorted_sets_to_sorted_lists_to_sets,  # / 3x
        )]


def only_intersections(a_range: int, b_range: int):
    print(f'***\ta_range: {a_range}, b_range: {b_range}\t***')
    [measure(fn, a_range, b_range, set, 10) for fn in (sets,)]
    [measure(fn, a_range, b_range, lambda i: set(sorted(i)), 10) for fn in (presorted_sets,)]
    [measure(fn, a_range, b_range, sorted, 10) for fn in (presorted_lists_to_set_a, presorted_lists_to_set_both)]
    [measure(fn, a_range, b_range, None, 10) for fn in
     (unsorted_lists_to_set_a, unsorted_lists_to_set_both, unsorted_sets_to_sorted_lists_to_sets)]


if __name__ == '__main__':
    only_intersections(100000, 10)
    only_intersections(100000, 100)
    only_intersections(100000, 1000)
    only_intersections(100000, 10000)

# ***  Conclusions
# *  If you already have sets, dont sort them
#     If you have lists, dont sort them either.
#     Intersecting sets is 3 orders of mag faster than creating sets out of lists, then intersecting.
#     O(n^2) intersecting is 4 orders of mag slower than creating sets out of lists, then intersecting.
