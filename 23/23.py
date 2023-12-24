import sys

sys.setrecursionlimit(100000)

path = 'input.txt'

grid = ()

with open(path, 'r') as file:
    grid = tuple([tuple(c.strip()) for c in file.readlines()])

def getStartEnd(g):
    return (0, g[0].index('.')), (len(g) - 1, g[len(g) - 1].index('.'))


def getMaxPath(grid, curPos, end, isClimbPossible, count = -1, visited = set(), path = [], shortcuts = set()):
    
    result = False
    curVisited = visited.copy()
    curVisited.add(curPos)
    nextPoss = []

    curPath = path.copy()

    isCut = False
    for shortcut in shortcuts:
        if shortcut[0] == curPos:
            curPos = shortcut[1]
            count += shortcut[2]
            isCut = True
            break
        elif shortcut[1] == curPos:
            curPos = shortcut[0]
            count += shortcut[2]
            isCut = True
            break

    if not isCut:
        count += 1

    if curPos == end:
        return True, count
    
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for dir in dirs:
        nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])

        if nextPos[0] < 0 or nextPos[0] >= len(grid) or nextPos[1] < 0 or nextPos[1] >= len(grid[0]):
            continue

        if nextPos in curVisited:
            continue

        nextC = grid[nextPos[0]][nextPos[1]]

        if nextC == '#':
            continue

        if nextC in ('^', 'v', '>', '<'):
            slope = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
            
            if not isClimbPossible and dir != slope[nextC]:
                continue

            nextnextPos = (nextPos[0] + slope[nextC][0], nextPos[1] + slope[nextC][0])
            if nextnextPos in curVisited:
                continue
        
        nextPoss.append(nextPos)

    if len(nextPoss) <= 1:
        curPath.append(curPos)
    elif len(curPath) >= 2:
        shortcuts.add((curPath[0], curPath[-1], len(curPath)))
        curPath = []

    counts = [0]
    for nextPos in nextPoss:
        nextResult, newCount = getMaxPath(grid, nextPos, end, isClimbPossible, count, curVisited, curPath, shortcuts)
        if nextResult:
            counts.append(newCount)
            result = True


    return result, max(counts)



def part1(start, end, grid):
    """ part 1 """

    res, maxPath = getMaxPath(grid, start, end, False)

    return maxPath

    
def part2(start, end, grid):
    """ part 2 """

    res, maxPath = getMaxPath(grid, start, end, True)

    return maxPath


start, end = getStartEnd(grid)

print(part1(start, end, grid))
print(part2(start, end, grid))