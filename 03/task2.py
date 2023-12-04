from day import Day
from collections import defaultdict

def nei(x,y):

    neigh_2d_4 = ((x-1,y), (x+1,y), (x, y-1), (x, y+1))
    neigh_2d_5 = neigh_2d_4  + ((x,y),)
    neigh_2d_4_skew = ((x-1,y-1), (x+1,y-1), (x-1, y+1), (x+1, y+1))
    neigh_2d_8 = neigh_2d_4  + neigh_2d_4_skew
    neigh_2d_9 = neigh_2d_8 + ((x,y),)
    return neigh_2d_9
day = Day(3)
# day = Day(3,'ex.in')
touching = []
gears = []
for j, d in enumerate(day.lines):
    # find position of anyy character in string that is not a dot or a digit
    indeces = [i for i, c in enumerate(d) if c == '*']
    for i in indeces:
        gears.append((i, j))

gears_to_numbers = defaultdict(list)
for (i,j) in gears:
    neigh = nei(i,j)
    tested = set()
    for x,y in neigh:

        if (x,y) in tested:
            continue
        if y<0 or y>=len(day.lines):
            continue
        if x<0 or x>=len(day.lines[y]):
            continue
        if day.lines[y][x].isdigit():
            d = day.lines[y]
            start = x
            tested |= {(x,y)}
            while start-1 >= 0 and d[start-1].isdigit():
                start -= 1
                tested |= {(start,y)}
            end = x
            while end+1 < len(d) and d[end+1].isdigit():
                end += 1
                tested |= {(end,y)}
            extracted = d[start:end+1]
            print(f"start: {start}, end: {end}, extracted: {extracted}, i: {i}, j: {j}")
            number = int(extracted)
            gears_to_numbers[(i,j)].append(number)
ratios = []
for k,v in gears_to_numbers.items():
    print(k,v)
    if len(v)==2:
        ratios.append(v[0]*v[1])

print(ratios)
res = sum(ratios)
print(res)
day//res
