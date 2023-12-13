path = 'input.txt'

grids = []

with open(path, 'r') as file:
    grids = file.read().split('\n\n')

    for i, grid in enumerate(grids):
        grids[i] = grid.split('\n')

def solve(grids, useOneOff):
    def getMirrorLines(grid, useOneOff):
        def checkMirrorRow(grid, rowl, rowr, useOneOff, oneOffLeft):
            if rowl < 0 or rowr >= len(grid):
                if useOneOff:
                    return not oneOffLeft, oneOffLeft
                return True, oneOffLeft
            result, oneOffLeft = compareRows(grid, rowl, rowr, oneOffLeft)
            if result:
                return checkMirrorRow(grid, rowl - 1, rowr + 1, useOneOff, oneOffLeft)
            return False, oneOffLeft
        
        def checkMirrorCol(grid, coll, colr, useOneOff, oneOffLeft):
            if coll < 0 or colr >= len(grid[0]):
                if useOneOff:
                    return not oneOffLeft, oneOffLeft
                return True, oneOffLeft
            result, oneOffLeft = compareCols(grid, coll, colr, oneOffLeft)
            if result:
                return checkMirrorCol(grid, coll - 1, colr + 1, useOneOff, oneOffLeft)
            return False, oneOffLeft
        
        def compareRows(grid, row1, row2, oneOffLeft):
            equal = 0
            for c1, c2 in zip(grid[row1], grid[row2]):
                if c1 == c2:
                    equal += 1

            if equal + 1 == len(grid[0]) and oneOffLeft:
                return True, False

            return equal == len(grid[0]), oneOffLeft
        
        def compareCols(grid, col1, col2, oneOffLeft):
            equal = 0
            for i in range(len(grid)):
                if grid[i][col1] == grid[i][col2]:
                    equal += 1

            if equal + 1 == len(grid) and oneOffLeft:
                return True, False

            return equal == len(grid), oneOffLeft

        rows = -1
        cols = -1

        for i in range(len(grid[:-1])):
            oneOffLeft = useOneOff
            result, oneOffLeft = compareRows(grid, i, i + 1, oneOffLeft)
            if result:
                result, oneOffLeft = checkMirrorRow(grid, i - 1, i + 2, useOneOff, oneOffLeft)
                if result:
                    rows = i + 1
                    break

        for i in range(len(grid[0]) - 1):
            oneOffLeft = useOneOff
            result, oneOffLeft = compareCols(grid, i, i + 1, oneOffLeft)
            if result:
                result, oneOffLeft = checkMirrorCol(grid, i - 1, i + 2, useOneOff, oneOffLeft)
                if result:
                    cols = i + 1
                    break

        return rows, cols
    
    
    result = 0

    for grid in grids:
        rows, cols = getMirrorLines(grid, useOneOff)
        if rows != -1:
            result += 100 * rows
        if cols != -1:
            result += cols

    return result



def part1(grids):
    """ part 1 """
    return solve(grids, False)

    
    
def part2(grids):
    """ part 2 """

    return solve(grids, True)

print(part1(grids))
print(part2(grids))