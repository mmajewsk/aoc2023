
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
    path = [(0,0)]
    a,b = 0,0
    for direction, length, color in data:
        if p2 == True:
            value = int(color[2:-2], 16)
            direction = "RDLU"[int(color[-2])]
            length = value
        if direction == "R":
            a += int(length)
        elif direction == "L":
            a -= int(length)
        elif direction == "U":
            b += int(length)
        elif direction == "D":
            b -= int(length)
        path.append((a,b))
    return path


def path_to_area(path):
    area = 0
    pathlen = 0
    for i in range(len(path)-1):
        x1,y1 = path[i]
        x2,y2 = path[i+1]
        area += x1*y2 - x2*y1
        ppl = abs(x1-x2) + abs(y1-y2)
        pathlen += ppl
    area = abs(area)
    real_area = area- (area-pathlen-1)//2
    return real_area


p1 = path_to_area(data_to_path(data))
p2 = path_to_area(data_to_path(data, p2=True))
print(p1)
print(p2)
