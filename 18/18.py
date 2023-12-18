path = 'input.txt'

dirs = []
lengths = []
colors = []

with open(path, 'r') as file:
    for row in file:
        dir, length, color = row.split()
        dirs.append(dir)
        lengths.append(int(length))
        colors.append(color[2:8])

def dig(dirs, lengths):
    def getArea(holes):

        shoelaceArea = abs(sum((h1[0] + h2[0])*(h1[1] - h2[1]) / 2 for h1, h2 in zip(holes, holes[1:])))
        return int(shoelaceArea + len(holes) / 2 + 1)

    holes = []
    curRow = 0
    curCol = 0

    dirConv = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    
    for dir, length in zip(dirs,lengths):
        for i in range(length):
            holes.append((curRow, curCol))
            curRow += dirConv[dir][0]
            curCol += dirConv[dir][1]
    
    return getArea(holes)


def part1(dirs, lengths):
    """ part 1 """

    return dig(dirs, lengths)
    
    
def part2(colors):
    """ part 2 """

    dirs = []
    lengths = []

    conv = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

    for color in colors:
        dirs.append(conv[color[-1]])
        lengths.append(int(color[0:5], 16))
    
    return dig(dirs, lengths)

print(part1(dirs, lengths))
print(part2(colors))