"""
4. Consecutive Sum

Find the number of ways an integer can be represented as the sum of two or more consecutive integers.
Given a long integer, find the number of ways to represent it as a sum of two or more consecutive positive integers.

For example, consider the number 21. It can be expressed as the sums of [1, 2, 3, 4, 5, 6], [6, 7, 8] and [10, 11].
There are 3 ways to sum to 21 using consecutive positive integers.


#### 1. Function Description ####

Complete the function consecutive in the editor below.
The function must return an integer denoting the number of ways to represent num as a 
sum of two or more consecutive positive integers.

Consecutive has the following parameter(s):
- num: the integer to sum to


#### 2. Constraints ####

1 ≤ num ≤ 10 12

* Input Format For Custom Testing *

Locked stub code in the editor reads from stdin and passes it to the function.
There is one line containing num, the integer to process.

## a. Sample Case 0 ##

Sample Input: 15
Sample Output: 3

* Explanation 0 *

There are three ways to calculate num = 15 as a sum of two or more consecutive integers:
- 1 + 2 + 3 + 4 + 5 = 15
- 4 + 5 + 6 = 15
- 7 + 8 = 15
Thus, the function returns 3.

## b. Sample Case 1 ##

Sample Input: 10
Sample Output: 1

* Explanation 1 *

There is one way to calculate num = 10 as a sum of two or more consecutive integers:
- 1 + 2 + 3 + 4 = 10
Thus, the function returns 1.

## c. Additional Test Cases ##
0. Input: 15
Output: 3

1. Input: 10
Output: 1

2. Input: 250
Output: 3

"""

#!/bin/python3

import math, os, random, re, sys

#
# Complete the 'consecutive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER num as parameter.
#

def consecutive(num):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    num = int(input().strip())
    result = consecutive(num)
    fptr.write(str(result) + '\n')
    fptr.close()
