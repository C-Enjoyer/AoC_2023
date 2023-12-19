path = 'input.txt'

wfs = {}
parts = []

with open(path, 'r') as file:
    for row in file:
        if row.strip() == "":
            continue
        elif row.startswith('{'):
            valDict = {}
            for kv in row.strip()[1:-1].split(','):
                key, value = kv.split('=')
                valDict[key] = int(value)
            parts.append(valDict)
        else:
            key, rest = row.strip().split('{')
            rest = rest.strip('}')
            conds = []
            end = ""
            for item in rest.split(','):
                if '<' in item or '>' in item:
                    c = '<' if '<' in item else '>'
                    var, value, next = item.split(c)[0], item.split(c)[1].split(':')[0], item.split(':')[1]
                    conds.append((var, c, int(value), next))
                else:
                    end = item
            wfs[key] = (conds, end)

def checkPart(wfs, curWf, part):
    def checkWf(curWf, part):

        wf = wfs[curWf]
        for cond in wf[0]:
            var, c, value, next = cond
            if (c == '<' and part[var] < value) or (c == '>' and part[var] > value):
                return next
        
        return wf[1]  

    while True:
        curWf = checkWf(curWf, part)
        if curWf == 'A' or curWf == 'R':
            return curWf == 'A'
        
def getPossible(wfs, curWf, curRanges):
    
    if curWf == 'R':
        return 0
    
    if curWf == 'A':
        prod = 1
        for min, max in curRanges.values():
            prod *= max - min + 1

        return prod

    wf = wfs[curWf]
    possible = 0

    for cond in wf[0]:
        var, c, value, next = cond
        newRanges = curRanges.copy()
        curMin, curMax = curRanges[var]

        if not (curMin < value < curMax):
            continue

        if c == '<':
            newRanges[var] = (curMin, value - 1)
            curRanges[var] = (value, curMax)

        elif c == '>':
            newRanges[var] = (value + 1, curMax)
            curRanges[var] = (curMin, value)

        possible += getPossible(wfs, next, newRanges)
    
    return possible + getPossible(wfs, wf[1], curRanges)

def part1(wfs, parts):
    """ part 1 """

    sum = 0
    
    for part in parts:
        if checkPart(wfs, "in", part):
            sum += part['x'] + part['m'] + part['a'] + part['s']
    
    return sum
    
def part2(wfs):
    """ part 2 """

    curRanges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

    return getPossible(wfs, "in", curRanges)

print(part1(wfs, parts))
print(part2(wfs))