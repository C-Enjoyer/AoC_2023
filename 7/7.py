from functools import cmp_to_key
from itertools import product

path = 'input.txt'

cardToInt = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
cardToIntJoker = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
hands = []

with open(path, 'r') as file:
    for row in file:
        hand, bid = row.split()
        hands.append((hand, int(bid)))

def compareHands(hand1, hand2, withJoker):
    def getValue(hand, withJoker):
        def findOccurrence(search, occurrences, withJoker):
            def getCombos(occurrences, jokers):
                
                possibilities = []
                for combo in product(range(jokers + 1), repeat = len(occurrences)):
                    if sum(combo) == jokers:
                        possibility = [a + b for a, b in zip(occurrences, combo)]
                        possibilities.append(possibility)
                return possibilities
        
            jokerNum = occurrences.get('J', 0)
            if withJoker and jokerNum:
                if jokerNum >= sum(search):
                    return True
                otherNum = {key: value for key, value in occurrences.items() if key != 'J'}
                combos = getCombos(list(otherNum.values()), jokerNum)
                for combo in combos:
                    if findOccurrence(search, dict(zip(otherNum.keys(), combo)), False):
                        return True
                return False
                
            else:
                allValues = list(occurrences.values())
                for item in set(search):
                    if search.count(item) > allValues.count(item):
                        return False
                return True

        occurrences = {}

        for card in hand:
            occurrences[card] = occurrences.get(card, 0) + 1
        
        if findOccurrence([5], occurrences, withJoker):
            return 6
        if findOccurrence([4], occurrences, withJoker):
            return 5
        if findOccurrence([3, 2], occurrences, withJoker):
            return 4
        if findOccurrence([3], occurrences, withJoker):
            return 3
        if findOccurrence([2, 2], occurrences, withJoker):
            return 2
        if findOccurrence([2], occurrences, withJoker):
            return 1
        
        return 0
    
    val1 = getValue(hand1[0], withJoker)
    val2 = getValue(hand2[0], withJoker)

    if(val1 > val2):
        return 1
    if(val2 > val1):
        return -1
    
    toInt = cardToIntJoker if withJoker else cardToInt
    
    for card1, card2 in zip(hand1[0], hand2[0]):
        if toInt[card1] > toInt[card2]:
            return 1
        if toInt[card2] > toInt[card1]:
            return -1

    return 0

def compareHandsWithJoker(hand1, hand2):
    return compareHands(hand1, hand2, True)

def compareHandsWithoutJoker(hand1, hand2):
    return compareHands(hand1, hand2, False)

def getWinnings(hands, withJoker):
    
    sortedHands = sorted(hands, key = cmp_to_key(compareHandsWithJoker if withJoker else compareHandsWithoutJoker))

    sum = 0
    
    for i, hand in enumerate(sortedHands):
        sum += (i + 1) * hand[1]

    return sum

def part1(hands):
    """ part 1 """
    return getWinnings(hands, False)
    
def part2(hands):
    """ part 2 """
    return getWinnings(hands, True)

print(part1(hands))
print(part2(hands))