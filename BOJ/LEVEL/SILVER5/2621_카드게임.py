from collections import Counter

cards = []
for _ in range(5):
    color, number = input().split()
    cards.append({
        "color": color, "num": int(number)
    })

cards.sort(key=lambda x: x["num"])


def isColorEquivalent(cards):
    prev = cards[0]['color']
    for i in range(1, len(cards)):
        if prev != cards[i]['color']:
            return False
        else:
            prev = cards[i]['color']
    return prev


def isNumContinuous(cards):
    prev = cards[0]['num']
    for i in range(1, len(cards)):
        if prev+1 != cards[i]['num']:
            return False
        prev = cards[i]['num']
    return True


def sameNumCounter(cards):
    def numPicker(d):
        return d['num']
    nums = list(map(numPicker, cards))
    return Counter(nums).most_common(2)


def rule15(cards):
    if isNumContinuous(cards):  # rule5
        if isColorEquivalent(cards):  # rule1
            return cards[-1]['num'] + 900
        return cards[-1]['num'] + 500
    return 0


def rule4(card):
    if isColorEquivalent(card):  # rule4
        return cards[-1]['num'] + 600
    return 0


def ruleSameNumber(cards):
    max, next = sameNumCounter(cards)
    if max[1] == 4 and next[1] == 1:  # rule 2
        return 800 + max[0]
    elif max[1] == 3 and next[1] == 2:  # rule 3
        return 700 + max[0]*10 + next[0]
    elif max[1] == 3 and next[1] == 1:  # rule7
        return 400 + max[0]
    elif max[1] == 2 and next[1] == 2:  # rule6
        if max[0] > next[0]:
            return 300 + max[0]*10 + next[0]
        else:
            return 300 + next[0]*10 + max[0]
    elif max[1] == 2 and next[1] == 1:  # rule8
        return 200+max[0]
    return 0


def ruleElse(cards):
    return cards[-1]['num'] + 100


candidates = [rule15(cards), rule4(
    cards), ruleSameNumber(cards), ruleElse(cards)]
# print(candidates)
print(max(candidates))
