path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        l.append(row.strip())

def part1(list):
    """ part 1 """
    sum = 0

    for line in list:
        digits = [c for c in line if c.isdigit()]
        sum += int(digits[0] + digits[-1])

    return sum
    
def part2(list):
    """ part 2 """
    sum = 0

    lut = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for line in list:
        digits = []
        for i in range(len(line)):
            
            if line[i].isdigit():
                digits.append(line[i])
            
            for key in lut.keys():
                if line[i:].startswith(key):
                    digits.append(lut[key])
        
        sum += int(digits[0] + digits[-1])

    return sum

print(part1(l))
print(part2(l))