from itertools import combinations

path = 'input.txt'

grid = []

with open(path, 'r') as file:
    lines = file.readlines()
    grid = [list(line.strip()) for line in lines]

def offsetGalaxies(grid, offset):
    def findGalaxies(grid):
        galaxies = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == '#':
                    galaxies.append([r, c])
        return galaxies

    galaxies = findGalaxies(grid)

    emptyRows = [i for i, row in enumerate(grid) if all(cell == '.' for cell in row)]
    emptyColumns = [i for i in range(len(grid[0])) if all(row[i] == '.' for row in grid)]

    emptyRows.append(len(grid))
    emptyColumns.append(len(grid[0]))

    for gi in range(len(galaxies)):
        
        for ei in range(len(emptyRows[:-1])):
            if emptyRows[ei] < galaxies[gi][0] < emptyRows[ei + 1]:
                galaxies[gi][0] += offset * (ei + 1)
                break

        for ei in range(len(emptyColumns[:-1])):
            if emptyColumns[ei] < galaxies[gi][1] < emptyColumns[ei + 1]:
                galaxies[gi][1] += offset * (ei + 1)
                break

    return galaxies

def getDistances(galaxies):
    distances = 0

    for pair in list(combinations(galaxies, 2)):
        distances += abs(pair[0][0] - pair[1][0])
        distances += abs(pair[0][1] - pair[1][1])
    
    return distances


def part1(grid):
    """ part 1 """

    return getDistances(offsetGalaxies(grid, 1))

def part2(grid):
    """ part 2 """
    
    return getDistances(offsetGalaxies(grid, 1000000 - 1))

print(part1(grid))
print(part2(grid))