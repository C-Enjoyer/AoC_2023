path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        l.append(row.strip())

def getWins(line):
    beforePipe, afterPipe = line.split('|')
    winNums = [int(num) for num in beforePipe.split(':')[1].split()]
    nums = [int(num) for num in afterPipe.split()]
    return len(set(winNums) & set(nums))

def part1(list):
    """ part 1 """

    sum = 0

    for line in list:
        wins = getWins(line)
        if wins:
            sum += pow(2, wins - 1)
    
    return sum

    
def part2(list):
    """ part 2 """

    cards = [1] * len(list)

    for i, line in enumerate(list):
        wins = getWins(line)
        for j in range(1, wins + 1):
            cards[i+j] += cards[i]
    
    return sum(cards)

print(part1(l))
print(part2(l))