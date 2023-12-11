from day import Day
from collections import defaultdict, Counter
import numpy as np

# day = Day(11)
day = Day(11, 'ex.in')

data = []

sub = {
    '.': 0,
    "#": 1,

}
for l in day.lines:
    data.append([sub[n] for n in l])

def expand(data):
    x = data.sum(axis=0)
    y = data.sum(axis=1)
    zeroind_x = np.where(x == 0)[0] + 1
    zeroind_y = np.where(y == 0)[0] + 1

    # print(x,y)
    # print(zeroind_x, zeroind_y)

    data2 = data.copy()
    # print(data)
    for e,i in enumerate(zeroind_x):
        data2 =  np.insert(data2, i+e, np.zeros_like(x), axis=1)
        # print(i)
        # print(data2)

    for e,i in enumerate(zeroind_y):
        data2 =  np.insert(data2, i+e, np.zeros_like(data2[0]), axis=0)
        # print(i)
        # print(data2)
    return data2
data_np = np.array(data)
data_epanded = expand(data_np)

# get nonzero indices in data_expanded
nonzero_ind = np.where(data_epanded != 0)
a,b =  nonzero_ind
tuples = list(zip(a,b))
from itertools import combinations
# print(tuples)
combinations = list(combinations(tuples,2))


# print(combinations)
sums = []
for a,b  in combinations:
    ax, ay = a
    bx, by = b
    diff_x = bx - ax
    diff_y = by - ay
    l = abs(diff_x) + abs(diff_y)
    sums.append(l)
    print(f"a: {a}, b: {b}, l: {l}, diff_x: {diff_x}, diff_y: {diff_y}, l: {l}")

print(sum(sums))
