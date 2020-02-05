"""
1. Jumping Jack

Jumping Jack is standing at the bottom of an infinite stairway.
He wants to see how high he can climb.
There are some rules of movement, however.
First, there is one bad step somewhere on the stairway.
Jack must avoid jumping on that step.
Second, he has a limited number of moves he must make.
At each move, his action will be either to jump a number of steps or remain where he is.
Either way, the number of steps he can jump in one move increments by one each time.

For example, assume Jumping Jack is at the bottom of a staircase at position 0.
He needs to avoid the step at position 6.

Scenario 1:  His first jump can be one step. He takes it and lands at step 1.
His second jump can be two steps. That will put him at step 3, so he takes it.
His next jump can be three steps. He would land on step 6, so he decides to wait until the next move.
His next jump can be 4 steps, so he takes it to step 7 and continues to jump up the stairs.

Scenario 2:  Jack first decision is to remain at step 0. He then jumps two to land at step 2, three to land at 5.
His next jump of four steps will land him at step 9, again having successfully avoided step 6
and he can safely continue up the stairway.

Notice that in Scenario 2, he reaches step 9 on his fourth move whereas he landed at step 7 in Scenario 1.
Your task involves maximizing the step Jumping Jack will land on after a given number of moves. 
He would choose to act as Scenario 2 describes.


#### 1. Function Description ####

Complete the function maxStep in the editor below.
The function must return an integer that denotes the maximum step number Jack can reach from step 0
if he performs exactly n actions and never jumps on step k.

maxStep has the following parameter(s):
- n:  integer, the number actions Jack must take
- k:  integer, the position of the bad step


#### 2. Constraints ####

- 1 ≤ n ≤ 2 × 10^3
- 1 ≤ k ≤ 4 × 10^6

* Input Format for Custom Testing *
Input from stdin will be processed as follows and passed to the function.

The first line contains an integer n, the number of actions Jack must take.
The next line contains an integer k, the number of the step he must avoid.


#### 3. Test Cases ####

## a. Sample Case 0 ##

* Sample Input 0 *
[2, 2]

* Sample Output 0 *
3

* Explanation 0 *
Jack performs the following sequence of n = 2 actions:

- Jack jumps from step 0 to step 0 + 1 = 1.
- Jack jumps from step 1 to step 1 + 2 = 3; he avoided step k = 2 by jumping over it.


## b. Sample Case 1 ##

* Sample Input 1 *
[2, 1]

* Sample Output 1 *
2

* Explanation 1 *
Jack performs the following sequence of n = 2 actions:
- Jack cannot jump onto step 1 because k = 1.
He can only jump 1 step during his first action, so he stays on step 0.
- Jack jumps from step 0 to step 0 + 2 = 2.


## c. Sample Case 2 ##

* Sample Input 2 *
[3, 3]

* Sample Output 2 *
5

* Explanation 2 * 
Jack must skip some jump because performing one jump during each step will land him on step k = 3 on the second jump.
There are two ways for him to perform all n = 3 actions:
- For the first action, jump 1 unit to step 0 + 1 = 1. For the second action, remain at step 1.
For the third action, jump 3 units to step 1 + 3 = 4. In other words, his sequence of actions is 0 → 1 → 1 → 4.
- For the first action, remain at step 0. For the second action, jump 2 units to step 0 + 2 = 2.
For the third action, jump 3 units to step 2 + 3 = 5. In other words, his sequence of actions is 0 → 0 → 2 → 5.

The maximal step number that Jack can reach by performing any sequence of possible actions is 5.


## d. Additional Test Cases ##

0. Input: [2, 2]
Output: 3

1. Input: [2, 1]
Output: 2
"""

#!/bin/python3

import math, os, random, re, sys

#
# Complete the 'maxStep' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def maxStep(n, k):
    # Write your code here
    result = 0

    for i in range(n + 1):
        if result == k:
            result -= 1
        result += i
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    k = int(input().strip())
    result = maxStep(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()