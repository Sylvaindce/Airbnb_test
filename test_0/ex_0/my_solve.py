#!/bin/python3

import math, os, random, re, sys

#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

class robot(object):

    def __init__(self):
        self.__xy = [0, 0]

        # WEST, NORTH, EAST, SOUTH
        self.__orientation = [0, 1, 0, 0]

    def move(self, cmd):
        if cmd == 'G':
            self.__apply()
        elif cmd == 'L':
            self.__change_direction(False)
        elif cmd == 'G':
            self.__change_direction(True)
    
    def __change_direction(self, direction):
        if direction:
            self.__orientation[0], self.__orientation[1:] = self.__orientation[-1], self.__orientation[:-1]
            return
        self.__orientation[-1], self.__orientation[:-1] = self.__orientation[0], self.__orientation[1:]
    
    def __apply(self):
        index = self.__orientation.index(1)
        add_val = 1
        if index in [0, 3]:
            add_val = -1
        self.__xy[index % 2] += add_val

    @property
    def state(self):
        return [self.__xy, self.__orientation]

    def __str__(self):
        return "X: %d - Y: %d - Orientation: %s" % (self.__xy[0], self.__xy[1], str(self.__orientation))

def doesCircleExist(commands):
    result = [None] * len(commands)

    for i, cmds in enumerate(commands):
        rob = robot()
        for cmd in cmds:
            rob.move(cmd)
            print(rob)
        if rob.state[0] == [0, 0]:
            result[i] = "YES"
            continue
        result[i] = "NO"
    
    return result

if __name__ == "__main__":
    print(doesCircleExist(["G"]))
    #print(doesCircleExist(["RGRGRGRG"]))

"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    commands_count = int(input().strip())

    commands = []

    for _ in range(commands_count):
        commands_item = input()
        commands.append(commands_item)

    result = doesCircleExist(commands)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
"""