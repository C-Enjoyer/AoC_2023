path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        l.append(row.strip())

def part1(list):
    """ part 1 """
    sum = 0

    def checkGame(game):
        sets = game.split(';')

        for set in sets:
            for item in set.split(','):
                count, color = item.strip().split()

                if color == 'red':
                    if int(count) > 12:
                        return False
                elif color == 'green':
                    if int(count) > 13:
                        return False
                elif color == 'blue':
                    if int(count) > 14:
                        return False
        
        return True

    for line in list:
        parts = line.split(':')
        num = int(parts[0].split()[1])

        if checkGame(parts[1]):
            sum += num

    return sum


    
def part2(list):
    """ part 2 """
    sum = 0

    def getPower(game):
        sets = game.split(';')
        r, g, b = 0, 0, 0

        for set in sets:
            for item in set.split(','):
                count, color = item.strip().split()

                if color == 'red':
                    r = max(r, int(count))
                elif color == 'green':
                    g = max(g, int(count))
                elif color == 'blue':
                    b = max(b, int(count))
        
        return r * g * b


    for line in list:
        sum += getPower(line.split(':')[1])

    return sum

print(part1(l))
print(part2(l))