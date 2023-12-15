path = 'input.txt'

strings = []

with open(path, 'r') as file:
    for row in file:
        strings.extend([string for string in row.strip().split(',')])

def getHash(string):
    strVal = 0
    for c in string:
        strVal += ord(c)
        strVal *= 17
        strVal %= 256
    return strVal

def part1(strings):
    """ part 1 """

    result = 0
    
    for string in strings:
        result += getHash(string)

    return result

    
def part2(strings):
    """ part 2 """

    boxes = [{} for _ in range(256)]

    for string in strings:
        if '=' in string:
            label, num = string.split('=')
            hash = getHash(label)
            boxes[hash][label] = int(num)

        elif '-' in string:
            label = string[:-1]
            hash = getHash(label)
            if label in boxes[hash]:
                del boxes[hash][label]

    result = 0

    for boxi, box in enumerate(boxes):
        for slot, (key, value) in enumerate(box.items()):
            result += (boxi + 1) * (slot + 1) * value

    return result

print(part1(strings))
print(part2(strings))