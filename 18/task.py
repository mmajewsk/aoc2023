data = list(map(str.split, open('ex.in')))

dir_to_complex = lambda x : {"R":1+0j, "L":-1+0j, "U":0+1j, "D":0-1j}[x]
p1_data = [(dir_to_complex(d), int(l)) for d,l,c in data]
p2_data = [(dir_to_complex("RDLU"[int(c[-2])]), int(c[2:-2], 16)) for d,l,c in data]

def data_to_path(data):
    x1, x2 = 0,0
    area, pathlen = 0,0
    for m, length in data:
        x2 += m*length
        # area += x1.real*x2.imag - x2.real*x1.imag
        area += (x1 * x2.conjugate()).imag
        ppl = x1-x2
        pathlen += abs(ppl)
        x1 = x2
    area = abs(area)
    real_area = area//2+pathlen//2+1
    return int(real_area)

p1 = data_to_path(p1_data)
p2 = data_to_path(p2_data)
print(p1)
print(p2)
