path = 'input.txt'

grid = ()
start = ()

with open(path, 'r') as file:
    lines = []
    for rowI, row in enumerate(file):
        pos = row.find("S")
        if pos != -1:
            row = row[:pos] + '.' + row[pos + 1:]
            start = (rowI, pos)
        lines.append(row.strip())

    grid = tuple(tuple(row) for row in lines)

def getChar(grid, pos):
    return grid[pos[0] % len(grid)][pos[1] % len(grid[0])]

def doStep(grid, positions, a):

    newPositions = set()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for position in positions:
        for dir in dirs:
            newPos = (position[0] + dir[0], position[1] + dir[1])
            if getChar(grid, newPos) == '.':
                newPositions.add(newPos)

    return newPositions

def doSteps(grid, start, steps, forPoly, polyNum):

    nextPositions = set()
    curPostitions = set()
    curPostitions.add(start)
    res = 0
    a = []

    for step in range(forPoly):
        
        if step == steps:
            res = len(curPostitions)

        nextPositions = doStep(grid, curPostitions, a)

        if step % len(grid) == forPoly % len(grid):
            a.append(len(curPostitions))
            if len(a) == polyNum:
                break

        curPostitions = nextPositions

    return res, a

def getQuad(a, n):
    return (n * (n - 1) // 2) * ((a[2] - a[1]) - (a[1] - a[0])) + (a[1] - a[0]) * n + a[0]


def part1(res):
    """ part 1 """

    return res
    
def part2(a):
    """ part 2 """

    return getQuad(a, 26501365 // len(grid))
    

res, a = doSteps(grid, start, 64, 26501365, 3)

print(part1(res))
print(part2(a))