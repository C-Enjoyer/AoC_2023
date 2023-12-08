import math

path = 'input.txt'

dirs = ""
knots = {}

with open(path, 'r') as file:
    lines = file.readlines()
    dirs = lines[0].strip()
    for line in lines[2:]:
        parts = [part.strip() for part in line.split('=')]
        knots[parts[0]] = [value.strip() for value in parts[1][1:-1].split(',')]

def getDistanceFromKnot(knot, knots, dirs, endStr):
    curKnot = tuple(knot)
    cnt = 0
    while not curKnot[0].endswith(endStr):
        dir = 0 if dirs[cnt % len(dirs)] == 'L' else 1
        curKnot = (curKnot[1][dir], knots[curKnot[1][dir]])
        cnt += 1
    return cnt


def part1(dirs, knots):
    """ part 1 """

    curKnot = ("AAA", knots["AAA"])
    return getDistanceFromKnot(curKnot, knots, dirs, "ZZZ")
    
def part2(dirs, knots):
    """ part 2 """

    curKnots = []
    
    for key, value in knots.items():
        if key.endswith('A'):
            curKnots.append((key, value))

    distances = []

    for curKnot in curKnots:
        distances.append(getDistanceFromKnot(curKnot, knots, dirs, "Z"))
    
    return math.lcm(*distances)

print(part1(dirs, knots))
print(part2(dirs, knots))