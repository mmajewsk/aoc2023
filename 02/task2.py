import numpy as np
import re
from collections import defaultdict, Counter

def parse(s):
    # parse the following string
    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # get game id, and the dict values separated by ;
    # example return: (1, {"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2})
    s = s.rstrip('\n')
    game_id = int(re.search(r"Game (\d+):", s).group(1))
    # split the string into 3 parts
    s = s.split(':')[1].split(";")
    shows= [  ]
    for show in s:
        print(show)
        spli = show.split(',')
        lspli = [x[1:].split()[::-1] for x in spli]
        sh = dict(lspli)
        di = {k: int(v) for k, v in sh.items()}
        assert len(di) <= 3
        shows.append(di)

    return game_id, shows


lines = open(0).readlines()
games = defaultdict(Counter)
for l in lines:
    gid, shows = parse(l)
    print(shows)
    games[gid] = shows
    # for sh in shows:
    #     games[gid] += Counter(sh)
powers = []
for gid, d in games.items():
    minshow = {'red': 0, 'green':0, 'blue':0}
    for show in d:
        for color, num in show.items():
            if minshow[color] == 0:
                minshow[color] = num
            else:
                minshow[color] = max(minshow[color], num)
    # power of set .setdefault(key, []).append(value)
    res = np.prod(list(minshow.values()))
    powers.append(res)
    print(f"minshow: {minshow}, power: {res}")
print(sum(powers))
