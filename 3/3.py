path = 'input.txt'

grid = []

with open(path, 'r') as file:
    for row in file:
        grid.append(list(row.strip()))

def part1(grid):
    """ part 1 """

    def checkPos(grid, pos):

        def checkRC(grid, row, col):
            rows = len(grid)
            cols = len(grid[0])

            check = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]

            for r, c in check:
                if 0 <= r < rows and 0 <= c < cols:
                    if grid[r][c] != '.' and not grid[r][c].isdigit():
                        return True

            return False


        for p in pos:
            if checkRC(grid, p[0], p[1]):
                return True

        return False


    sum = 0

    for row, line in enumerate(grid):
        num = ''
        pos = []
        for col, c in enumerate(line):
            if c.isdigit():
                num += c
                pos.append((row, col))
            
            if not c.isdigit() or col == len(line) - 1:
                if checkPos(grid, pos):
                    sum += int(num)
                num = ''
                pos.clear()

    return sum
    
def part2(grid):
    """ part 2 """

    def getNumbers(grid, row, col):

        def getNumber(line, pos):
            num = ''

            for i in range(pos, -1, -1):
                if not line[i].isdigit():
                    break
                num = line[i] + num

            for i in range(pos + 1, len(line)):
                if not line[i].isdigit():
                    break
                num += line[i]

            return int(num)

        nums = []
        rows = len(grid)
        cols = len(grid[0])

        check = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]

        for r, c in check:
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c].isdigit():
                    num = getNumber(grid[r], c)
                    if num not in nums:
                        nums.append(num)
                    
        return nums


    sum = 0

    for row, line in enumerate(grid):
        for col, c in enumerate(line):
            if c == '*':
                numbers = getNumbers(grid, row, col)
                if len(numbers) == 2:
                    sum += numbers[0] * numbers[1]

    return sum


print(part1(grid))
print(part2(grid))