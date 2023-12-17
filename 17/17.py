import heapq

path = 'input.txt'

grid = ()

with open(path, 'r') as file:
    grid = tuple(tuple(int(digit) for digit in line.strip()) for line in file.readlines())

def getMinPath(grid, start, end, minStraight, maxStraight):

    dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1) , 'W': (0, -1)}

    q = []
    q.append((0, 'E', start))
    q.append((0, 'S', start))

    visited = set()

    while q:
        curLen, curStraight, curPos = heapq.heappop(q)
        if (curPos, curStraight) in visited:
            continue

        visited.add((curPos, curStraight))

        for nextDir in dirs:
            nextPos = (curPos[0] + dirs[nextDir][0], curPos[1] + dirs[nextDir][1])
            nextRow = nextPos[0]
            nextCol = nextPos[1]
            lastDir = curStraight[-1]

            if nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0]):
                continue

            if lastDir != nextDir and len(curStraight) < minStraight:
                continue

            if lastDir == nextDir and len(curStraight) == maxStraight:
                continue

            if (lastDir == 'N' and nextDir == 'S') or (lastDir == 'S' and nextDir == 'N') or (lastDir == 'E' and nextDir == 'W') or (lastDir == 'W' and nextDir == 'E'):
                continue

            nextStraight = curStraight + nextDir if lastDir == nextDir else nextDir
                
            if (nextPos, nextStraight) in visited:
                continue

            nextLen = curLen + grid[nextRow][nextCol]
            
            if nextPos == end and len(nextStraight) >= minStraight:
                return nextLen

            heapq.heappush(q, (nextLen, nextStraight, nextPos))

    return -1

def part1(grid):
    """ part 1 """

    return getMinPath(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1), 1, 3)

    
def part2(grid):
    """ part 2 """
    
    return getMinPath(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1), 4, 10)

print(part1(grid))
print(part2(grid))