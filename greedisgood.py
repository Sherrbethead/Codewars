'''Description

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a "5" can only count as part of
a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.'''


def score(dice):
    points = 0
    for throw in dice:
        if dice.count(throw) >= 3 and throw != 1:
            points += int(str(throw) + '00')
            if dice.count(throw) > 3 and throw == 5:
                points -= 150
            break
        elif dice.count(throw) >= 3 and throw == 1:
            points += 1000
            if dice.count(throw) > 3:
                points -= 300
            break
    for throw in dice:
        if throw == 1 and dice.count(throw) != 3:
            points += 100
        elif throw == 5 and dice.count(throw) != 3:
            points += 50
    return points

print(score([2, 3, 4, 6, 2]))  # 0
print(score([2, 4, 4, 5, 4]))  # 450
print(score([1, 6, 1, 1, 1]))  # 1100