l = open("inp.txt").readlines()
# filter each line for digits

# p1
l = [list(filter(lambda x: x.isdigit(), i)) for i in l]
l = [i[0] + i[-1] for i in l]
l = [int(i) for i in l]
print(sum(l))

# p2
d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(len(l)):
    for j in d:
        l[i] = l[i].replace(j, j + str(d.index(j)) + j)
l = [list(filter(lambda x: x.isdigit(), i)) for i in l]
l = [i[0] + i[-1] for i in l]
l = [int(i) for i in l]
print(sum(l))
