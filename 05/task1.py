from day import Day
from collections import defaultdict

day = Day(5)
# day = Day(5, 'ex.in')
lines = day.lines
# split lines by empty line
seeds = lines[0]
lines = lines[2:]

seeds = seeds.split(':')[1].split(' ')
seeds = [int(s) for s in seeds if s != '']
# print(seeds)
textstart = False
textmap = defaultdict(list)
key = None
for l in lines:
    if 'map' in l:
        textstart = True
        key = tuple(l.split(' ')[0].split('-to-'))
        textmap[key] = []
    elif l == '':
        textstart = False
        key = None
        continue
    else:
        spl = l.split(' ')
        spl = [int(s) for s in spl]
        textmap[key].append(spl)
textmap2 = {}

for (a,b), values in textmap.items():
    tmpd = {'dest': [], 'sour': []}
    for dest, sour, r in values:
        tmpd['dest'].append((dest, dest+r-1))
        tmpd['sour'].append((sour, sour+r-1))
    textmap2[a] = (b, tmpd)

mappings = {}
for s in seeds:
    text = 'seed'
    start_seed = int(s)
    # print('start seed', s)
    while text != 'location':
        text, data = textmap2[text]
        for i, (low, high) in enumerate(data['sour']):
            if low <= s <= high:
                s = data['dest'][i][0] + s - low
                break
        # print(' ', text, s)
    mappings[start_seed] = s
print(mappings)
res = min(mappings.values())
print(res)
day/res
