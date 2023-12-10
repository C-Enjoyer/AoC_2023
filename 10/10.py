path = 'input.txt'

class coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __eq__(self, other):
        if not isinstance(other, coord):
            return False
        return self.row == other.row and self.col == other.col
        
grid = []
start = coord(-1, -1)

with open(path, 'r') as file:
    for rowI, row in enumerate(file):
        grid.append(list(row.strip()))
        for colI, col in enumerate(row):
            if col == 'S':
                start = coord(rowI, colI)

def getChar(grid, pos):
    if pos.row >= len(grid) or pos.row < 0 or pos.col >= len(grid[pos.row]) or pos.col < 0:
        return '.'
    return grid[pos.row][pos.col]

def isPossible(grid, pos1, pos2):
    c1 = getChar(grid, pos1)
    c2 = getChar(grid, pos2)
    if c1 == '.' or c2 == '.':
        return False

    N = c1 in ('|', '7', 'F', 'S') and c2 in ('|', 'L', 'J', 'S')
    E = c1 in ('-', 'J', '7', 'S') and c2 in ('-', 'L', 'F', 'S')
    S = c1 in ('|', 'L', 'J', 'S') and c2 in ('|', '7', 'F', 'S')
    W = c1 in ('-', 'L', 'F', 'S') and c2 in ('-', 'J', '7', 'S')

    return (N and pos1.row + 1 == pos2.row) or (E and pos1.col == pos2.col + 1) or (S and pos1.row == pos2.row + 1) or (W and pos1.col + 1 == pos2.col)

def getNext(grid, lastPos, curPos):
    for row, col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nextPos = coord(curPos.row + row, curPos.col + col)
        if nextPos == lastPos:
            continue
        if isPossible(grid, curPos, nextPos):
            return nextPos
    
    return coord(-1, -1) # we should not get here

def getPath(grid, start):
    curPos = start
    fromPos = coord(-1, -1)
    path = []
    binGrid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    while curPos != start or not len(path):
        path.append(curPos)
        binGrid[curPos.row][curPos.col] = True
        nextPos = getNext(grid, fromPos, curPos)

        fromPos = curPos
        curPos = nextPos
    
    return path, binGrid

def replaceStart(grid, start):
    N = isPossible(grid, start, coord(start.row - 1, start.col))
    S = isPossible(grid, start, coord(start.row + 1, start.col))
    E = isPossible(grid, start, coord(start.row, start.col + 1))
    W = isPossible(grid, start, coord(start.row, start.col - 1))

    if N and S:
        grid[start.row][start.col] = '|'
    elif E and W:
        grid[start.row][start.col] = '-'
    elif N and E:
        grid[start.row][start.col] = 'L'
    elif N and W:
        grid[start.row][start.col] = 'J'
    elif S and W:
        grid[start.row][start.col] = '7'
    elif S and E:
        grid[start.row][start.col] = 'F'

def part1(path):
    """ part 1 """

    return int(len(path) / 2)
    
def part2(grid, binGrid):
    """ part 2 """
    
    insideCnt = 0
    isInside = False
    beginCorner = ''

    for rowI, row in enumerate(binGrid):
        for colI, isPath in enumerate(row):

            if not isPath:
                if isInside:
                    insideCnt += 1
                continue

            c = grid[rowI][colI]

            if c == '|' or (beginCorner == 'L' and c == '7') or (beginCorner == 'F' and c == 'J'):
                isInside = not isInside
            elif c in ('L', 'F'):
                beginCorner = c

    return insideCnt


replaceStart(grid, start)
path, binGrid = getPath(grid, start)

print(part1(path))
print(part2(grid, binGrid))