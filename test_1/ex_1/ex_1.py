#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'commonPrefix' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.
#

def commonPrefix(inputs):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputs_count = int(input().strip())

    inputs = []

    for _ in range(inputs_count):
        inputs_item = input()
        inputs.append(inputs_item)

    result = commonPrefix(inputs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()