from day import Day
import math

# day= Day(4, 'ex.in')
day= Day(4)


results = []
for line in day.lines:
    a, b = line.split(':')
    winning, have = b.split('|')
    winning = winning.split(' ')
    have = have.split(' ')
    winning = [int(x.strip()) for x in winning if x.strip() != '']
    have = [int(x.strip()) for x in have if x.strip() != '']
    c = 0
    for h in have:
        if h in winning:
            c += 1
    points = math.floor(2**(c-1))
    results.append(points)
    print(winning, have, c, points)
print(sum(results))
day/sum(results)
