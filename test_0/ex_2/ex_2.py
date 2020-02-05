"""
3. Triangle Or Not?

A student is given 3 poles and has been asked to find out if they can form a non-degenerate triangle.
(https://en.wikipedia.org/wiki/Degeneracy_(mathematics)#Triangle)
If the 3 poles are placed with tips joined such that they form a triangle with non-zero angles at each vertex,
then a non-degenerate triangle is formed.

Poles with length [3, 4, 5] will make a non-degenerate triangle while [1, 1, 5] will not.


### 1. Function Description ###

Complete the function triangleOrNot in the editor below.
The function must return an array of n strings where the value at each index i is 
- Yes if a[i], b[i], and c[i] can form a non-degenerate triangle
- otherwise, it's No.

triangleOrNot has the following parameter(s):
- a[a[0],...a[n-1]]:  array of n integers where each index i describes the length of side a for triangle i
- b[b[0],...b[n-1]]:  array of n integers representing lengths of sides b[i]
- c[c[0],...c[n-1]]:  array of n integers representing lengths of sides c[i]


### 2. Constraints ###

- 1 ≤ n ≤ 10^5
- 1 ≤ a[i], b[i], c[i] ≤ 10^3, where 0 ≤ i < n


#### 3. Test Cases ####

Input Format For Custom Testing

Locked stub code reads input from stdin and passes it to the function.

The first line contains an integer, n, denoting the number of elements in a.
Each of the next n lines contains an integer a[i].

The next line contains an integer, n, denoting the number of elements in b.
Each of the next n lines contains an integer b[i].

The next line contains an integer, n, denoting the number of elements in c.
Each of the next n lines contains an integer c[i].
 

## a. Sample Case 0 ##

* Sample Input 0 *
[3, 7, 10, 7, 3, 2, 3, 4, 3, 2, 7, 4]

* Sample Output 0 *
[No, No, Yes]

* Explanation 0 *
We want to check the following n = 3 possible triangles using the values given by
a = [7, 10, 7], b = [2, 3, 4], and c = [2, 7, 4]:

- a[0] = 7, b[0] = 2, and c[0] = 2 don't form a valid,
non-degenerate triangle, so we store No in index 0 of our return array.

- a[1] = 10, b[1] = 3, and c[1] = 7 don't form a valid, non-degenerate triangle,
so we store No in index 1 of our return array.

- a[2]= 7, b[2]= 4, and c[2] = 4 do form a valid, non-degenerate triangle,
so we store Yes in index 2 of our return array.

We then return the array ["No", "No", "Yes"] as our answer.


## b. Additional Test Cases ##

0. Input: [3 7 10 7 3 2 3 4 3 2 7 4]
Output: ["No", "No", "Yes"]

1. Input: [7 10 1 9 4 5 6 10 7 5 7 3 9 4 10 10 7 5 4 8 10 1 8 8]
Output: ["No", "No", "Yes", "Yes", "No", "Yes", "Yes"]

2. Input: [5 1 3 6 2 6 5 8 10 3 2 4 5 7 3 7 9 10]
Output: ["No", "No", "Yes", "No", "No"]
"""

import sys, os

# Complete the function below.

def triangleOrNot(a, b, c):
    pass


if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a_cnt = 0
    a_cnt = int(input())
    a_i = 0
    a = []
    while a_i < a_cnt:
        a_item = int(input())
        a.append(a_item)
        a_i += 1


    b_cnt = 0
    b_cnt = int(input())
    b_i = 0
    b = []
    while b_i < b_cnt:
        b_item = int(input())
        b.append(b_item)
        b_i += 1


    c_cnt = 0
    c_cnt = int(input())
    c_i = 0
    c = []
    while c_i < c_cnt:
        c_item = int(input())
        c.append(c_item)
        c_i += 1

    res = triangleOrNot(a, b, c)
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()