
from day import Day
from collections import defaultdict, Counter
import numpy as np

# day = Day(18)
day = Day(18, 'ex.in')

data = []

for l in day.lines:
    direction, length, color = l.split(" ")
    data.append((direction, int(length), color))


def data_to_path(data, p2=False):
    path = [0]
    a = 0
    for direction, length, color in data:
        if p2 == True:
            value = int(color[2:-2], 16)
            direction = "RDLU"[int(color[-2])]
            length = value
        m = {"R":1+0j, "L":-1+0j, "U":0+1j, "D":0-1j}[direction]
        a += m*length
        path.append(a)
    return path


def path_to_area(path):
    area = 0
    pathlen = 0
    for i in range(len(path)-1):
        x1 = path[i]
        x2 = path[i+1]
        # area += x1.real*x2.imag - x2.real*x1.imag
        area += (x1 * x2.conjugate()).imag
        ppl = x1-x2
        pathlen += abs(ppl)
    area = abs(area)
    real_area = area//2+pathlen//2+1
    return int(real_area)


p1 = path_to_area(data_to_path(data))
p2 = path_to_area(data_to_path(data, p2=True))
print(p1)
print(p2)
