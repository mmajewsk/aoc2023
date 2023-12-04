from collections import defaultdict, Counter
import re
lines = open(0).readlines()

max_cubes = {
    "red": 12,
    "green":13,
    "blue": 14,
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
        sh = dict(re.findall(r"(\d+) (\w+)", show))
        di = {v: int(k) for k, v in sh.items()}
        assert len(di) <= 3
        shows.append(di)

    return game_id, shows




games = defaultdict(Counter)
for l in lines:
    gid, shows = parse(l)
    print(shows)
    games[gid] = shows
    # for sh in shows:
    #     games[gid] += Counter(sh)

# check if number exceeds max cubes
okgames = []
for gid, d in games.items():
    wrong = False
    for show in d:
        # lineviz = f"Game {gid}: "
        for color, num in show.items():
            if num > max_cubes[color]:
                wrong = True
                # lineviz += bcolors.RED+bcolors.BOLD+f"{color}: {num} "+bcolors.ENDC

            # else:
                # lineviz += f"{color}: {num} "
        # if sum(d.values()) > sum(max_cubes.values()):
        #     wrong = True
    if not wrong:
        okgames.append(int(gid))
    # print(lineviz)

print(okgames)
print(sum(okgames))
