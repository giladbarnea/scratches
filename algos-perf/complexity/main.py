from random import randint
from string import ascii_letters, punctuation
from more_itertools import random_combination_with_replacement

strings = ascii_letters + punctuation


def randstring():
    return ''.join(random_combination_with_replacement(strings, randint(1, 6)))


def generate_randoms():
    # build 100K randoms
    randoms = []
    for _ in range(10000):
        if randint(0, 1):
            # random string
            randoms.append(randstring())
        else:
            randoms.append(randint(0, 1000000))
    return randoms


def build(typ):
    if typ is dict:
        return dict.fromkeys(generate_randoms(), None)
    else:
        return typ(generate_randoms())

# TODO in IPython:
#  d = build(deque)
#  %%timeit -n1
#       for random in generate_randoms():
#       random in s


# *** timeit
# import timeit
#
# timed = timeit.timeit("""
# for random in generate_randoms():
#     random in d
# """, setup="""
# from collections import deque
#
# from random import randint
# from string import ascii_letters, punctuation
# from more_itertools import random_combination_with_replacement
#
# strings = ascii_letters + punctuation
#
#
# def randstring():
#     return ''.join(random_combination_with_replacement(strings, randint(1, 6)))
#
#
# def generate_randoms():
#     # build 100K randoms
#     randoms = []
#     for _ in range(10000):
#         if randint(0, 1):
#             # random string
#             randoms.append(randstring())
#         else:
#             randoms.append(randint(0, 1000000))
#     return randoms
#
#
# d = deque(generate_randoms())
# """, number=10)
#
# print(timed)


# *** pd + matplotlib
# import pandas as pd
# import pickle
# from pathlib import Path
# deque_pickle_path = Path('./deque.pickle')
# if deque_pickle_path.exists():
#     with open(deque_pickle_path, mode='rb') as f:
#         deque_pickle = pickle.load(f)
# else:
#     deque_check = timeit.timeit('check()', f'from __main__ import check, build_deque; d = build_deque()', number=100)
#     with open(deque_pickle_path, mode='xb') as f:
#         pickle.dump(deque_check, f)
#
# df = pd.DataFrame({'index': index_runs, 'iter': it_runs}, index=r)
# df.plot()
