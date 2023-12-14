from functools import cache

path = 'input.txt'

grid = []

with open(path, 'r') as file:
    for row in file:
        grid.append(list(row.strip()))

@cache
def cycle(g):
    @cache
    def rotateGridCw(g):
        return tuple(tuple(row[::-1]) for row in zip(*g))
    
    for i in range(4):
        g = fallNorth(g)
        g = rotateGridCw(g)
    return g

@cache
def fallNorth(g):
    g = [list(row) for row in g]
    for col in range(len(g[0])):
        lowRow = 0
        for row in range(len(g)):
            if g[row][col] == 'O':
                g[row][col] = '.'
                g[lowRow][col] = 'O'
                lowRow += 1
            elif g[row][col] == '#':
                lowRow = row + 1

    return tuple(tuple(row) for row in g)

@cache
def getWeight(g):
    weigth = 0
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == 'O':
                weigth += len(grid) - row
    
    return weigth

def part1(g):
    """ part 1 """
    g = fallNorth(g)
    return getWeight(g)
    
def part2(g):
    """ part 2 """
    cycles = 1000000000
    gs = []
    for rot in range(cycles):
        gs.append(g)
        g = cycle(g)
        if g in gs:
            index = gs.index(g)
            cur = rot + 1
            return getWeight(gs[index + (cycles - cur) % (cur - index)])
    
    return -1

grid = tuple(tuple(row) for row in grid)
print(part1(grid))
print(part2(grid))