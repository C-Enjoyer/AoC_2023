path = 'input.txt'

grid = ()

with open(path, 'r') as file:
    grid = tuple([tuple(row.strip()) for row in file])

def getPoints(grid, prevRow, prevCol, row, col):
    seen = set()
    q = []
    q.append((prevRow, prevCol, row, col))

    while q:
        nextQ = []
        cur = q.pop(0)
        prevRow, prevCol, row, col = cur
        
        seen.add(cur)

        if grid[row][col] == '/':
            nextQ.append((row, col, row - (col - prevCol), col - (row - prevRow)))
        elif grid[row][col] == '\\':
            nextQ.append((row, col, row + (col - prevCol), col + (row - prevRow)))
        elif grid[row][col] == '|' and col != prevCol:
            nextQ.append((row, col, row - 1, col))
            nextQ.append((row, col, row + 1, col))
        elif grid[row][col] == '-' and row != prevRow:
            nextQ.append((row, col, row, col - 1))
            nextQ.append((row, col, row, col + 1))
        else:
            nextQ.append((row, col, row + (row - prevRow), col + (col - prevCol)))

        for cur in nextQ:
            prevRow, prevCol, row, col = cur
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if cur in seen:
                continue

            q.append(cur)
    
    return len(set((row, col) for _, _, row, col in seen))


def part1(grid):
    """ part 1 """

    return getPoints(grid, 0, -1, 0, 0)


def part2(grid):
    """ part 2 """

    points = []

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        points.append(getPoints(grid, row, -1, row, 0))
        points.append(getPoints(grid, row, cols, row, cols - 1))

    for col in range(cols):
        points.append(getPoints(grid, -1, col, 0, col))
        points.append(getPoints(grid, rows, col, rows - 1, col))

    return max(points)

print(part1(grid))
print(part2(grid))