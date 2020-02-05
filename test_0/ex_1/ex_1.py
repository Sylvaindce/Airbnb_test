"""
2. Searching Trees

Determine if an element is present in a Binary Search Tree.

In a binary search tree, each node holds a value and a reference to as many as 2 child nodes,
or children. The root node has no ancestors. 
The children are called left and right, and subtrees rooted at left and right are the left and right subtrees.
If each node is considered the root of a subtree, each node value in its left subtree must be less than its own value.
Likewise, each node in its right subtree must have a greater or equal value to the root.
This allows for efficient searching.

For each value in a list of integers, determine if it is present in a tree.
If it is, return the integer 1, otherwise, return 0.


### 1. Function Description ###

Complete the function isPresent in the editor below.
The function must return 1 if the value is present in the BST, or 0 if it's not.

isPresent has the following parameter(s):
    - root:  reference to the root node of a tree of integers
    - val:  integer to search for


### 2. Constraints ###

- 1 ≤ total nodes ≤ 10^5
- 1 ≤ val ≤ 5 × 10^4

* Input Format for Custom Testing *
Input from stdin will be processed as follows and passed to the function:

The first line contains an integer, n, the number of elements in the tree.
Each of the next n lines contains an integer, the value of node[i] where 0 ≤ i ≤ n and node[i] is the root
The next line contains an integer, q, the number of queries
Each of the next q lines contains an integer to search for


#### 3. Test Cases ####

## a. Sample Case 0 ##

* Sample Input 0 *

[11, 20, 10, 30, 8, 12, 25, 40, 6, 11, 13, 23, 4, 30, 10, 12, 15]

refs:
https://static.hackerrank.com/recruit/questions/342/image_1.png
https://hrcdn.net/s3_pub/istreet-assets/LyWskEp_qXmkeoO5UxaaTw/searchingtree.svg

* Test Values *

[30, 10, 12, 15]

* Sample Output 0 *
[1, 1, 1, 0]

* Explanation *
The tree is assembled as described in Input Format for Custom Testing by the provided code stub.
Nodes marked "Nil" have no value and are placeholders to make left and right clear.
Tests for values 30, 10, 12, 15 should return 1, 1, 1, 0 respectively where 1 means the value is in the tree and 0 means it is not.


## b. Sample Case 1 ##

* Sample Input 1 *

[11, 20, 10, 30, 8, 12, 25, 40, 6, 11, 13, 23, 4, 30, 10, 12, 15]

refs:
https://static.hackerrank.com/recruit/questions/342/image_1.png"

* Test Values *
[79, 10, 20, 30, 40]

* Sample Output 1 *
[0, 1, 1, 1, 1]

* Explanation *
The tree is the same as in Sample 0.
The tests for values 79, 10, 20, 30, 40 should return 0, 1, 1, 1, 1 respectively.

## c. Additional Test Cases ##

0. Input: [11 20 10 30 8 12 25 40 6 11 13 23 4 30 10 12 15]
Output: [1 1 1 0]

1. Input: [11 20 10 30 8 12 25 40 6 11 13 23 5 79 10 20 30 40]
Output: [0 1 1 1 1]

2. Input: [10 14 12 10 9 17 22 16 19 5 6 5 13 22 15 17 9]
Output: [0 1 0 1 1]

"""

class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data)
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data)
    return node


"""
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
"""

def isPresent (root,val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    return

_a = None
_a_size =int(input())
_a_i=0

while _a_i < _a_size:
    _a_item = int(input())
    _a = _insert_node_into_binarysearchtree(_a, _a_item)
    _a_i += 1

q = int(input())
i = 0

while i < q:
    _b = int(input())
    _result = isPresent(_a , _b)
    print(_result)
    i += 1