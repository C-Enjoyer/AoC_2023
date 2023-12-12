from functools import cache

path = 'input.txt'

inputs = []
hints = []

with open(path, 'r') as file:
    for row in file:
        input, hint = row.strip().split()
        inputs.append(input)
        hints.append(tuple([int(num) for num in hint.split(',')]))

@cache
def getCombinations(input, hint, done):
    if not input:
        return int(not hint and not done)
    
    combinations = 0
    possible = [".", "#"] if input[0] == "?" else input[0]
    for c in possible:
        if c == "#":
            combinations += getCombinations(input[1:], hint, done + 1)
        else:
            if done:
                if hint and hint[0] == done:
                    combinations += getCombinations(input[1:], hint[1:], 0)
            else:
                combinations += getCombinations(input[1:], hint, 0)
    return combinations

def part1(inputs, hints):
    """ part 1 """

    result = 0

    for input, hint in zip(inputs, hints):
        result += getCombinations(input + '.', hint, 0)
    
    return result

    
def part2(inputs, hints):
    """ part 2 """

    factor = 5

    result = 0

    for input, hint in zip(inputs, hints):
        result += getCombinations("?".join([input] * 5) + '.', hint * factor, 0)
    
    return result


print(part1(inputs, hints))
print(part2(inputs, hints))