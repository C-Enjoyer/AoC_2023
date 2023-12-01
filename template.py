path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        num = int(row.strip())
        l.append(num)

def part1(list):
    """ part 1 """
    
def part2(list):
    """ part 2 """

print(part1(l))
print(part2(l))