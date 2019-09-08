'''Description

Introduction
A multi-storey car park (also called a parking garage, parking structure, parking ramp, parkade, parking building,
parking deck or indoor parking) is a building designed for car parking and where there are a number of floors or levels
on which parking takes place. It is essentially an indoor, stacked car park. Parking structures may be heated if they
are enclosed. Design of parking structures can add considerable cost for planning new developments, and can be mandated
by cities or states in new building parking requirements. Some cities such as London have abolished previously enacted
minimum parking requirements (Source Wikipedia)
Task
Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the
edge of the levels (you’re not Superman!) and the exit is always on the far right of the ground floor.
Rules
1. You are passed the carpark data as an argument into the function.
2. Free carparking spaces are represented by a 0
3. Staircases are represented by a 1
4. Your parking place (start position) is represented by a 2
5. The exit is always the far right element of the ground floor.
6. You must use the staircases to go down a level.
7. You will never start on a staircase.
8. The start level may be any level of the car park.
9. Each floor will have only one staircase apart from the ground floor which will not have any staircases.
Returns
Return an array of the quickest route out of the carpark
R1 = Move Right one parking space.
L1 = Move Left one parking space.
D1 = Move Down one level.
Example
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
You start in the most far right position on level 1
You have to move Left 4 places to reach the staircase => "L4"
You then go down one flight of stairs => "D1"
To escape you have to move Right 4 places => "R4"'''


def escape(carpark):
    result = list()
    stairscount = 1
    for i in range(len(carpark)):
        if carpark[i].count(2):
            place = i
    for j in range(place, len(carpark)):
        if not carpark[place].count(1):
            move = carpark[j].index(2) - (len(carpark[j]) - 1)
            if move:
                result.append('R' + str(abs(move)))
        else:
            if j != len(carpark) - 1:
                stairs = carpark[j].index(1)
                if j == place:
                    move = carpark[j].index(2) - stairs
                    if move > 0:
                        result.append('L' + str(abs(move)))
                    else:
                        result.append('R' + str(abs(move)))
                else:
                    move = carpark[j-1].index(1) - stairs
                    if move:
                        result.append('D' + str(stairscount))
                        if move > 0:
                            result.append('L' + str(abs(move)))
                        else:
                            result.append('R' + str(abs(move)))
                        stairscount = 1
                    else:
                        stairscount += 1
            else:
                move = carpark[j-1].index(1) - (len(carpark[j]) - 1)
                result.append('D' + str(stairscount))
                if move:
                    result.append('R' + str(abs(move)))
                else:
                    continue
    return result

print(escape([[0, 2, 0, 0, 1],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]]))  # ['R3', 'D3']
print(escape([[1, 0, 0, 0, 2],
              [0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]))  # ['L4', 'D1', 'R4', 'D1', 'L4', 'D1', 'R4']
