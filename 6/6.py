path = 'input.txt'

lines = []

with open(path, 'r') as file:
    lines = file.readlines()

def solve(times, distances):
    def getPossible(time, distance):
        def checkPossible(holdTime, time, distance):
            return (time - holdTime) * holdTime > distance
        
        first = -1
        last = -1
        for i in range(time):
            if(checkPossible(i, time, distance)):
                first = i
                break
        
        for i in range(time - 1, -1, -1):
            if(checkPossible(i, time, distance)):
                last = i
                break

        return list(range(first, last + 1))

    sum = 1

    for time, distance in zip(times, distances):
        sum *= len(getPossible(time, distance))

    return sum

def part1(lines):
    """ part 1 """
    times = [int(num) for num in lines[0].split(':')[1].split()]
    distances = [int(num) for num in lines[1].split(':')[1].split()]

    return solve(times, distances)

    
def part2(lines):
    """ part 2 """
    def parseLine(line):
        return int(''.join(char for char in line if char.isdigit()))
    
    time = parseLine(lines[0])
    distance = parseLine(lines[1])

    return solve([time], [distance])

print(part1(lines))
print(part2(lines))