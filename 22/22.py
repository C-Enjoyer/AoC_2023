path = 'input.txt'

bricks = []

with open(path, 'r') as file:
    for id, row in enumerate(file):
        l, r = row.strip().split('~')
        bricks.append(((tuple([int(num) for num in l.split(',')])), tuple([int(num) for num in r.split(',')]), id))

def fall(bricks):
    n = len(bricks)
 
    supports = {i: [] for i in range(n)}
    supportedBy = {i: [] for i in range(n)}
 
    settled = {}
 
    for brick in bricks:
        (x1, y1, z1), (x2, y2, z2), id = brick
 
        supporters = []
        while z1 > 1 and len(supporters) == 0:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        if (x, y, z - 1) in settled:
                            supporters.append((x, y, z - 1))
 
            if len(supporters) == 0:
                z1 -= 1
                z2 -= 1
 
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    settled[(x, y, z)] = id
 
        for sId in set(settled[sup] for sup in supporters):
            supports[sId].append(id)
            supportedBy[id].append(sId)
 
    return supports, supportedBy

def countRemovable(supports, supportedBy):
    
    cnt = 0

    for id in supports:
        canBeRemoved = True
        for sId in supports[id]:
            if len(supportedBy[sId]) == 1:
                canBeRemoved = False
                break
 
        if canBeRemoved:
            cnt += 1
 
    return cnt

def countChainReaction(supports, supportedBy):
    
    cnt = 0

    for id in supports:
        toCheck = supports[id].copy()
        falling = {id}
 
        while toCheck:
            curId = toCheck.pop(0)
 
            if all(sId in falling for sId in supportedBy[curId]):
                falling.add(curId)
                toCheck += supports[curId]
 
        cnt += len(falling) - 1
 
    return cnt

def part1(supports, supportedBy):
    """ part 1 """

    return countRemovable(supports, supportedBy)
    
    
    
def part2(supports, supportedBy):
    """ part 2 """

    return countChainReaction(supports, supportedBy)

bricks.sort(key = lambda b: b[0][2])
supports, supportedBy = fall(bricks)

print(part1(supports, supportedBy))
print(part2(supports, supportedBy))