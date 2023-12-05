# from day import Day
from collections import defaultdict
# from tqdm import tqdm

# day = Day(5)
# day = Day(5, 'ex.in')
# source = 'ex.in'
source = 'p5.in'
lines = open(source).read().splitlines()
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
inverse_map = {}

for (a,b), values in textmap.items():
    tmpd = {'dest': [], 'sour': []}
    for dest, sour, r in values:
        tmpd['dest'].append((dest, dest+r-1))
        tmpd['sour'].append((sour, sour+r-1))
    zippered = sorted(zip(tmpd['dest'], tmpd['sour']), key=lambda x: x[0][0])
    tmpd['dest'], tmpd['sour'] = zip(*zippered)
    inverse_map[b] = (a, tmpd)

## don't even ask

levels= []
text = 'location'
while text != 'seed':
    text, data = inverse_map[text]
    lambdas = []
    fundef = 'def foo(x):\n'
    for j, (low, high) in enumerate(data['dest']):
        newmin =  data['sour'][j][0]
        adder = newmin - low
        clause = f"    if {low} <= x <= {high}:\n        return {adder}+x\n"
        fundef += clause
    fundef += '    return x\n'
    exec(fundef)
    print(fundef)
    levels.append(foo)

def maxfoo(x):
    for foo in levels:
        x = foo(x)
    return x



seeds_range = []
for x in range(0,len(seeds),2):
    seeds_range.append((seeds[x], seeds[x]+seeds[x+1]-1))
print(seeds_range)

print(levels)

# for i in tqdm(range(20000000,30000000)):
for i in range(0,3640772818 * 1000):
    if i % 1000000 == 0:
        print(i)
    isin = False
    s = maxfoo(i)
    for low, high in seeds_range:
        if low <= s <= high:
            isin = True
            break
        if isin:
            break
    if isin:
        break
print(i, s, isin)

# day/res
