#!/bin/python3

import math
import os
import random
import re
import sys

def get_common_prefix_length_recursif(string='', suffix=0, lenght=0):
    for i in range(len(string[suffix:])):
        if string[suffix:][i] != string[i]:
            break
        lenght += 1
    if suffix < len(string):
        return get_common_prefix_length_recursif(string, suffix + 1, lenght)
    return lenght

def get_common_prefix_length(string=''):
    lenght = 0
    limit = string
    while limit:
        for i in range(len(limit)):
            if limit[i] != string[i]:
                break
            lenght += 1
        limit = limit[1:]
    return lenght

def get_common_prefix_lenght_regex(string=''):
    lenght = 0
    limit = string
    while limit:
        try:
            res = re.match(r'^' + limit[0] + r"[" + limit[1:] + "]*", string, re.MULTILINE)
        except:
            res = re.match(r'^' + limit[0], string)
        #print(limit, res)
        try:
            lenght += res.end()
        except:
            pass
        limit = limit[1:]
    return lenght

def commonPrefix(inputs):
    result = [None] * len(inputs)

    for i in range(len(result)):
        #result[i] = get_common_prefix_length_recursif(inputs[i])
        #result[i] = get_common_prefix_lenght_regex(inputs[i])
        result[i] = get_common_prefix_length(inputs[i])

    return result

if __name__ == '__main__':
    #print(commonPrefix(["abcabcd"]))
    print(commonPrefix(["ababaa"]))