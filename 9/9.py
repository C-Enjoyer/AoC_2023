path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        l.append([int(num) for num in row.split()])


def getNext(difs):

    if all(dif == 0 for dif in difs):
        return 0
        
    return difs[-1] + getNext([difs[i + 1] - difs[i] for i in range(len(difs[:-1]))])

def part1(l):
    """ part 1 """

    return sum([getNext(nums) for nums in l])
    
def part2(l):
    """ part 2 """
    
    return sum([getNext(list(reversed(nums))) for nums in l])

print(part1(l))
print(part2(l))