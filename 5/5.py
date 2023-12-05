path = 'input.txt'

lines = []
seeds = []
converters = []

with open(path, 'r') as file:
    lines = [row.strip() for row in file if row.strip()]

def parseInput(lines):
    seeds = [int(num) for num in lines[0].split(':')[1].split()]
    converters = [[]]

    curConv = 0
    for i in range(2, len(lines)):
        if lines[i].endswith("map:"):
            curConv += 1
            converters.append([])
        else:
            converters[curConv].append([int(num) for num in lines[i].split()])
    
    return seeds, converters

def part1(seeds, converters):
    """ part 1 """

    list = seeds.copy()

    for converter in converters:
        for i, num in enumerate(list):
            for rule in converter:
                if rule[1] <= num <= rule[1] + rule[2] - 1:
                    list[i] = rule[0] + num - rule[1]
                    break

    return min(list)

def part2(seeds, converters):
    """ part 2 """

    def getParts(numMin, numMax, ruleMin, ruleMax):
        outRanges = []
        inRange = []

        if numMax < ruleMin or numMin > ruleMax:
            outRanges.append([numMin, numMax - numMin + 1])
        elif numMin >= ruleMin and numMax <= ruleMax:
            inRange= [numMin, numMax - numMin + 1]
        else:
            if numMin < ruleMin:
                outRanges.append([numMin, ruleMin - numMin])
            if numMin <= ruleMax and numMax >= ruleMin:
                inRange = [max(numMin, ruleMin), min(numMax, ruleMax) - max(numMin, ruleMin) + 1]
            if numMax > ruleMax:
                outRanges.append([ruleMax + 1, numMax - ruleMax])

        return outRanges, inRange
    
    ranges = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
    leftRanges = []

    for converter in converters:
        nextRanges = []
        for rule in converter:
            leftRanges = []
            for seedRange in ranges:
                outRanges, inRange = getParts(seedRange[0], seedRange[0] + seedRange[1] - 1, rule[1], rule[1] + rule[2] - 1)

                if len(inRange):
                    inRange[0] = rule[0] + inRange[0] - rule[1]
                    nextRanges.append(inRange)

                leftRanges.extend(outRanges)

            ranges = leftRanges
            
        nextRanges.extend(ranges)
        ranges = nextRanges

    return min(range[0] for range in ranges)
    
seeds, converters = parseInput(lines)
print(part1(seeds, converters))
print(part2(seeds, converters))