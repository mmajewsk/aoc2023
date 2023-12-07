
from day import Day
from collections import defaultdict, Counter
# from tqdm import tqdm

day = Day(7)
# day = Day(7, 'ex.in')


lines = day.lines

# time = [int(s) for s in lines[0].split(' ') if s.isdigit()]
# distance = [int(s) for s in lines[1].split(' ') if s.isdigit()]

hands = []
for l in lines:
    hand, bid = l.split(' ')
    hands.append((hand, int(bid)))

# print(hands)
def full(x):
    c = Counter(x)
    if len(c.keys()) != 2:
        return False
    elif len(c.keys()) == 2:
        vals = set(list(c.values()))
        return vals == {2,3}
    return False

def three_of_a_kind(x):
    c = Counter(x)
    if len(c.keys()) != 3:
        return False
    elif len(c.keys()) == 3:
        vals = set(list(c.values()))
        return vals == {1,3}
    return False

def two_pair(x):
    c = Counter(x)
    if len(c.keys()) != 3:
        return False
    elif len(c.keys()) == 3:
        vals = set(list(c.values()))
        return vals == {1,2,2}
    return False

def five_of_a_kind(x):
    return len(set(x)) == 1

def four_of_a_kind(x):
    return len(set(x)) == 2 and {1, 4}==set(Counter(x).values())

def one_pair(x):
    return len(set(x)) == 4

def high_card(x):
    return len(set(x)) == 5

kinds_rules = {
    # all five characters are the same
    "Five of a kind" : five_of_a_kind,
    # four of the five characters are the same
    "Four of a kind": four_of_a_kind,
    # three of the five characters are the same, but remaining two are also the same
    "Full house": full,
    "Three of a kind": three_of_a_kind,
    "Two pair" : two_pair,
    "One pair": one_pair,
    "High card": high_card
}

kinds_ordering = [
    # all five characters are the same
    "Five of a kind",
    # four of the five characters are the same
    "Four of a kind",
    # three of the five characters are the same, but remaining two are also the same
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

# for hand, bid in hands:
#     stronges = []
#     for i, kind in enumerate(kinds_ordering):
#         rule = kinds_rules[kind]
#         newhand = hand.replace('J', '')
#         c = Counter(newhand)
#         torep = c.most_common(1)[0][0]
#         newhand2 = hand.replace('J', torep)
#         isthis = rule(hand)
#         stronges.append((isthis, (hand,bid)))

#     kinds[kind].append((hand, bid))
print(kinds)

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
broken = False
for kind in reversed(kinds_ordering):
    if kind in sorted_kinds.keys():
        ordered.extend(sorted_kinds[kind])
    else:
        broken = True

sums = []
print(ordered)
for i, (hand, bid) in enumerate(ordered):
    sums.append((i+1)*bid)
print(sum(sums))
print(broken)
# day/sum(sums)
#299175475
#296679587
