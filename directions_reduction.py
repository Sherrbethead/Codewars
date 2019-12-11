"""
Description

Once upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. The directions
were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite,
"WEST" and "EAST" too. Going to one direction and coming back the opposite
direction is a needless effort. Since this is the wild west, with dreadful
weather and not much water, it's important to save yourself some energy,
otherwise you might die of thirst!
The directions given to the man are, for example, the following:
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
You can immediately see that going "NORTH" and then "SOUTH" is not reasonable,
better stay to the same place! So the task is to give to the man a simplified
version of the plan. A better plan in this case is simply: ["WEST"]
Task:
Write a function dir_reduc which will take an array of strings and returns an
array of strings with the needless directions removed (W<->E or S<->N side by
side).
Note:
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"]
is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST"
are not directly opposite of each other and can't become such.
Hence the result path is itself: ["NORTH", "WEST", "SOUTH", "EAST"].
"""


def dir_reduc(arr):
    stack = list()
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if (stack[-1] == 'NORTH' and i == 'SOUTH') or \
                    (stack[-1] == 'SOUTH' and i == 'NORTH') or \
                    (stack[-1] == 'EAST' and i == 'WEST') or \
                    (stack[-1] == 'WEST' and i == 'EAST'):
                stack.pop()
            else:
                stack.append(i)
    return stack


print(dir_reduc([
    "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"
]))  # ['WEST']
print(dir_reduc([
    "SOUTH", "EAST", "NORTH", "WEST", "SOUTH", "NORTH"
]))  # ['SOUTH', 'EAST', 'NORTH', 'WEST']
