from day import Day
import math
from collections import Counter

# day= Day(4, 'ex.in')
day= Day(4)


instances = Counter()
results = []
for line in day.lines:
    a, b = line.split(':')
    a_number = a[len('Card'):]
    print(a_number)
    a_number = int(a_number)
    instances[a_number] += 1
    winning, have = b.split('|')
    winning = winning.split(' ')
    have = have.split(' ')
    winning = [int(x.strip()) for x in winning if x.strip() != '']
    have = [int(x.strip()) for x in have if x.strip() != '']
    c = 0
    for h in have:
        if h in winning:
            c += 1
    # points = math.floor(2**(c-1))
    added_counter = Counter()
    for k in range(c):
        added_counter[a_number + k + 1] += 1
    print(a_number, instances, added_counter.keys(), c)
    tmp_counter = Counter()
    for m in range(instances[a_number]):
        tmp_counter += added_counter
    instances += tmp_counter
print(instances)
res = sum(instances.values())
# print(sum(results))
print(res)
day//res
