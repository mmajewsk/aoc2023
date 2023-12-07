from day import Day
from collections import defaultdict, Counter

day = Day(7)
# day = Day(7, 'ex.in')


lines = day.lines
hands = []
for l in lines:
    hand, bid = l.split(' ')
    hands.append((hand, int(bid)))

# print(hands)
kinds_rules = {
    "Five of a kind": lambda x: len(set(x)) == 1,
    "Four of a kind": lambda x: len(set(x)) == 2 and {1, 4} == set(Counter(x).values()),
    "Full house": lambda x: len(set(x)) == 2 and {2, 3} == set(Counter(x).values()),
    "Three of a kind": lambda x: len(set(x)) == 3 and {1, 1, 3} == set(Counter(x).values()),
    "Two pair": lambda x: len(set(x)) == 3 and {2, 1} == set(Counter(x).values()),
    "One pair": lambda x: len(set(x)) == 4,
    "High card": lambda x: len(set(x)) == 5,
}

kinds_ordering = [
    "Five of a kind",
    "Four of a kind",
    "Full house",
    "Three of a kind",
    "Two pair",
    "One pair",
    "High card"
]

kinds = defaultdict(list)

for hand, bid in hands:
    newhand = hand.replace('J', '')
    c = Counter(newhand)
    if newhand != '':
        torep, count = c.most_common(1)[0]
        newhand2 = hand.replace('J', torep)
    else:
        newhand2 = 'JJJJJ'
    for i, kind in enumerate(kinds_ordering):
        rule = kinds_rules[kind]
        if rule(newhand2):
            kinds[kind].append((hand, bid))

def mykey(x):
    if x.isdigit():
        return int(x)
    else:
        return {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}[x]

def hand2key(hand):
    vaal = 0
    for i, x in enumerate(reversed(hand)):
        vaal += mykey(x) * 15**i
    return vaal

sorted_kinds = {}
for kind, l in kinds.items():
    sorted_kinds[kind] = sorted(l, key=lambda x: hand2key(x[0]))
    print(kind, sorted_kinds[kind])

ordered = []
for kind in reversed(kinds_ordering):
    if kind in sorted_kinds.keys():
        ordered.extend(sorted_kinds[kind])

sums = []
print(ordered)
for i, (hand, bid) in enumerate(ordered):
    sums.append((i+1)*bid)
print(sum(sums))
