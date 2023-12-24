import numpy as np
from itertools import combinations
import z3

path = 'input.txt'

hss = []

with open(path, 'r') as file:
    for row in file:
        row = row.strip().replace(" ", "")
        coords, velos = row.split('@')
        hss.append((tuple([int(coord) for coord in coords.split(',')]), tuple([int(velo) for velo in velos.split(',')])))
        
def doIntersect(hs1, hs2, area):

    (apx, apy, _), (avx, avy, _) = hs1
    (bpx, bpy, _), (bvx, bvy, _) = hs2

    try:
        y = (bpx - (bvx / bvy * bpy) + (avx / avy * apy) - apx) / ( avx / avy - bvx / bvy)
        x = ((y - apy) / avy) * avx + apx

        if area[0] <= x <= area[1] and area[0] <= y <= area[1]:
            if np.sign(x - apx) == np.sign(avx) and np.sign(y - apy) == np.sign(avy) and np.sign(x - bpx) == np.sign(bvx) and np.sign(y - bpy) == np.sign(bvy):
                return True
            
    except: pass

    return False

def part1(hss):
    """ part 1 """

    sum = 0

    for combi in combinations(hss, 2):
        if doIntersect(combi[0], combi[1], (200000000000000, 400000000000000)):
            sum += 1

    return sum

    
def part2(hss):
    """ part 2 """

    answer = 0

    solver = z3.Solver()
    x, y, z, vx, vy, vz = [z3.Int(var) for var in ["x", "y", "z", "vx", "vy", "vz"]]

    for i in range(4):
        (cpx, cpy, cpz), (cvx, cvy, cvz) = hss[i]

        t = z3.Int(f"t{i}")
        solver.add(t >= 0)
        solver.add(x + vx * t == cpx + cvx * t)
        solver.add(y + vy * t == cpy + cvy * t)
        solver.add(z + vz * t == cpz + cvz * t)

    if solver.check() == z3.sat:
        model = solver.model()
        (x, y, z) = (model.eval(x), model.eval(y), model.eval(z))
        answer = x.as_long() + y.as_long() + z.as_long()

    return answer

print(part1(hss))
print(part2(hss))