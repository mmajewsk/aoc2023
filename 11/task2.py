from day import Day
from collections import defaultdict, Counter
import numpy as np

day = Day(11)
# day = Day(11, 'ex.in')

data = []

sub = {
    '.': 0,
    "#": 1,

}
for l in day.lines:
    data.append([sub[n] for n in l])

def indeces(data):
    x = data.sum(axis=0)
    y = data.sum(axis=1)
    zeroind_x = np.where(x == 0)[0]
    zeroind_y = np.where(y == 0)[0]
    return zeroind_x, zeroind_y
data_np = np.array(data)

exp_y, exp_x = indeces(data_np)

nonzero_ind = np.where(data_np != 0)
a,b =  nonzero_ind
tuples = list(zip(a,b))
from itertools import combinations
# print(tuples)
combinations = list(combinations(tuples,2))

def check_how_many_x_between(ax, bx):
    s = 0
    ax, bx = sorted((ax, bx))
    for ex in exp_x:
        if ax < ex < bx:
            # print(f"ax: {ax}, ex: {ex}, bx: {bx}")
            s += 1
    return s

def check_how_many_y_between(ay, by):
    s = 0
    ay, by = sorted((ay, by))
    for ey in exp_y:
        # print(ey)
        if ay < ey < by:
            # print(f"ay: {ay}, ey: {ey}, by: {by}")
            s += 1
    return s

# print(combinations)
print(exp_x, exp_y)
sums = []
multiplier = 1000000
# multiplier = 2
for a,b  in combinations:
    ax, ay = a
    bx, by = b
    xs = check_how_many_x_between(ax, bx)
    ys = check_how_many_y_between(ay, by)
    xsum = xs * (multiplier-1)
    ysum = ys * (multiplier-1)
    diff_x = bx - ax
    diff_y = by - ay
    l = abs(diff_x) + abs(diff_y) + xsum + ysum
    # print(a,b,diff_x, diff_y, xsum, ysum, l)
    # print(f"a: {ax, ay}, b: {bx, by}, xsum: {xsum}, ysum: {ysum}, diff_x: {diff_x}, diff_y: {diff_y}, l: {l}")
    sums.append(l)

print(data_np)
print(exp_x, exp_y)
print(sum(sums))
# p1 9734203
