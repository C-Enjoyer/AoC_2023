import copy
import math

path = 'input.txt'

mods = {}

with open(path, 'r') as file:
    for row in file:
        op = 'b'
        if row.startswith('%') or row.startswith('&'):
            op = row[0]
            row = row[1:]

        name, othersStr = row.strip().replace(" ", "").split('->')
        next = [other for other in othersStr.split(',')]
        prev = []

        mods[name] = [op, next, prev, False]


def setPrevs(modules):

    for module, values in modules.items():
        for next in values[1]:
            if next not in modules:
                break
            modules[next][2].append(module)

    return modules

def pressButton(modules, sentPulse, searchList = []):
    
    lowCnt = int(not sentPulse)
    highCnt = int(sentPulse)

    resDict = {element: False for element in searchList}

    for sentPulse, curMod in [(sentPulse, mod) for mod in modules["broadcaster"][1]]:
        q = [(sentPulse, curMod)]

        while q:
            
            sentPulse, curMod = q.pop(0)

            lowCnt += int(not sentPulse)
            highCnt += int(sentPulse)

            if curMod not in modules:
                continue

            if modules[curMod][0] == 'b':
                modules[curMod][3] = sentPulse
            
            elif modules[curMod][0] == '%':
                if sentPulse:
                    continue
                else:
                    modules[curMod][3] = not modules[curMod][3]

            elif modules[curMod][0] == '&':
                cnt = 0
                for prev in modules[curMod][2]:
                    cnt += int(modules[prev][3])

                modules[curMod][3] = cnt != len(modules[curMod][2])
            
            for next in modules[curMod][1]:
                q.append((modules[curMod][3], next))

            for mod in searchList:
                if curMod == mod and not modules[curMod][3]:
                    resDict[mod] = True

    return modules, resDict, lowCnt, highCnt

def getLastAndLayer(modules, curMod):
    
    lastAndLayer = []

    for key, values in modules.items():
        if curMod in values[1]:
            lastAndLayer.append(key)

    while True:
        lowerLayer = []
        for curMod in lastAndLayer:
            for prev in modules[curMod][2]:
                if modules[prev][0] == "%":
                    return lastAndLayer
            lowerLayer.extend(modules[curMod][2])
        lastAndLayer = lowerLayer.copy()


def part1(modules):
    """ part 1 """

    lowCnt = 0
    highCnt = 0

    for _ in range(1000):
        modules, _, nextLowCnt, nextHighCnt = pressButton(modules, False)
        lowCnt += nextLowCnt
        highCnt += nextHighCnt

    return lowCnt * highCnt
    
def part2(modules):
    """ part 2 """

    lastAndLayer = getLastAndLayer(modules, "rx")
    cycles = {element: 0 for element in lastAndLayer}
    cycle = 0

    while not all(value != 0 for value in cycles.values()):

        modules, resDict, _, _ = pressButton(modules, False, lastAndLayer)
        cycle += 1

        for curMod in lastAndLayer:
            if resDict[curMod]:
                cycles[curMod] = cycle
                lastAndLayer.remove(curMod)
       
    return math.lcm(*cycles.values())


mods = setPrevs(mods)
mods2 = copy.deepcopy(mods)

print(part1(mods))
print(part2(mods2))