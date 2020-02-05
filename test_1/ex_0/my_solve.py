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