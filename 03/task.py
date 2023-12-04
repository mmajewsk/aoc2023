from day import Day

def nei(x,y):

    neigh_2d_4 = ((x-1,y), (x+1,y), (x, y-1), (x, y+1))
    neigh_2d_5 = neigh_2d_4  + ((x,y),)
    neigh_2d_4_skew = ((x-1,y-1), (x+1,y-1), (x-1, y+1), (x+1, y+1))
    neigh_2d_8 = neigh_2d_4  + neigh_2d_4_skew
    neigh_2d_9 = neigh_2d_8 + ((x,y),)
    return neigh_2d_9
day = Day(3)
# day = Day(3,'ex.in')
symbols = []
touching = []
for j, d in enumerate(day.lines):
    # find position of anyy character in string that is not a dot or a digit
    indeces = [i for i, c in enumerate(d) if not (c == '.' or c.isdigit())]
    for i in indeces:
        symbols.append((i, j))
        touching += list(nei(i, j))

numbers = []
found = set()
fake = set()
for (i,j) in touching:
    if (i,j) in found:
        continue
    if (i,j) in fake:
        continue
    if day.lines[j][i].isdigit():
        d = day.lines[j]
        start = i
        found |= {(i,j)}
        while start-1 >= 0 and d[start-1].isdigit():
            start -= 1
            found |= {(start,j)}

        end = i
        while end+1 < len(d) and d[end+1].isdigit():
            end += 1
            found |= {(end,j)}
        extracted = d[start:end+1]
        print(f"start: {start}, end: {end}, extracted: {extracted}, i: {i}, j: {j}")
        number = int(extracted)
        numbers.append(number)
    else:
        fake |= {(i,j)}
print(numbers)
res = sum(numbers)
print(res)
# day/res
