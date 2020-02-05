"""
I. Encircular

Build a computer simulation of a mobile robot. The robot moves on an infinite plane, starting from position (0, 0). 
Its movements are described by a command string consisting of one or more of the following three letters:

- G instructs the robot to move forward one step.
- L instructs the robot to turn left in place.
- R instructs the robot to turn right in place.

The robot performs the instructions in a command sequence in an infinite loop. 
Determine whether there exists some circle such that the robot always moves within the circle.

Consider the commands R and G executed infinitely.
A diagram of the robot's movement looks like:

RG → RG
↑     ↓
RG ← RG

The robot will never leave the circle.


#### 1. Function Description ####

Complete the function doesCircleExist in the editor below.
The function must return an array of n strings either YES or NO based on whether the robot is bound within a circle or not, 
in order of test results.

doesCircleExist has the following parameter(s):

- commands[commands[0],...commands[n-1]]: 
  An array of n commands[i] where each represents a list of commands to test.


#### 2. Constraints ####

- 1 ≤ |commands[i]| ≤ 2500

- 1 ≤ n ≤ 10
- Each command consists of G, L, and R only.

Input from stdin will be processed as follows and passed to the function.
The first line contains an integer n, the number of elements in commands.

The next n lines each contain a string describing commands[i] where 0 ≤ i < n.


#### 3. Test Cases ####

## a. Sample Case 0 ##

* Sample Input 0 *
2 [GL]

* Sample Output 0 *
NO YES

* Explanation 0 *
There are n = 2 commands:

- For commands[0] = "G", the robot will move forward forever ( G → G → G →... ) without
  ever turning or being restricted to a circle. Set index 0 of the return array to NO.

- For commands[1] = "L", the robot will just turn 90 degrees left forever without ever 
  moving forward (because there is no "G" instruction). The robot is effectively trapped at one spot,
  thus bound within a circle. Set index 1 of the return array to YES.


## b. Sample Case 1 ##

* Sample Input 1 *
1 [GRGL]

* Sample Output 1 *
NO

* Explanation 1 *

Consider the robot's initial orientation to be facing north toward the positive y direction.
The robot performs the following four steps in a loop:

- Go forward one step. The robot moves from (0, 0) to (0, 1).
- Turn right. The robot turns eastward, facing the positive x direction.
- Go forward one step. The robot moves from (0, 1) to (1, 1).
- Turn left. The robot turns northward, facing the positive y direction again.

            ↑
      RG → LG
      ↑
RG → LG
↑
G

The robot then repeats these steps infinitely, following an endless zig-zag path in the northeasterly direction.
Because the robot will never turn in such a way that it would be restricted to a circle,
set index 0 of the return array to NO.


## c. Additional Test Cases ##

0. Input: [[G], [L]]
Output: No Yes

1. Input: [[GRGL]]
Output: No

2. Input: [[GGGGR], [RGL]]
Output: Yes No

"""

import os

def doesCircleExist(commands):
    return

if __name__ == '__main__':
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