#  Question-1:

# Given preorder of a binary tree, calculate its **[depth(or height)](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)** [starting from depth 0]. The preorder is given as a string with two possible characters.

# 1. ‘l’ denotes the leaf
# 2. ‘n’ denotes internal node

# The given tree can be seen as a full binary tree where every node has 0 or two children. The two children of a node can ‘n’ or ‘l’ or mix of both.

# **Examples :**

# Input  : nlnll
# Output : 2
# Explanation :

def calculate_depth(preorder):
    if not preorder:
        return 0

    n = len(preorder)

    
    def calculate_depth_recursive(index):
        if index >= n:
            return 0

        if preorder[index] == 'l':
            return 0

        left_index = index + 1
        right_index = index + 2

        left_depth = calculate_depth_recursive(left_index)
        right_depth = calculate_depth_recursive(right_index)

        return 1 + max(left_depth, right_depth)

    return calculate_depth_recursive(0)

preorder = 'nlnll'
depth = calculate_depth(preorder)
print(depth)


# Question-2:

# Given a Binary tree, the task is to print the **left view** of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.

# **Examples:**

# ***Input:***

#             4

#           /   \

#         5     2

#              /   \

#             3     1

#            /  \

#           6    7

# ***Output:** 4 5 3 6*


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view(root):
    if not root:
        return

    
    def left_view_recursive(node, level, max_level):
        if not node:
            return

        if level > max_level[0]:
            print(node.data, end=' ')
            max_level[0] = level

        left_view_recursive(node.left, level + 1, max_level)
        left_view_recursive(node.right, level + 1, max_level)

    max_level = [0]
    left_view_recursive(root, 1, max_level)


root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)

left_view(root)


#  Question-3:

# Given a Binary Tree, print the Right view of it.

# The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.

# **Examples:**

# **Input:**

#          1

#       /     \

#    2         3

# /   \       /  \

# 4     5   6    7

#              \

#                8

# **Output**: 

# Right view of the tree is 1 3 7 8

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_view(root):
    if not root:
        return

   
    def right_view_recursive(node, level, max_level):
        if not node:
            return

        if level > max_level[0]:
            print(node.data, end=' ')
            max_level[0] = level

        right_view_recursive(node.right, level + 1, max_level)
        right_view_recursive(node.left, level + 1, max_level)

    max_level = [0]
    right_view_recursive(root, 1, max_level)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

right_view(root)



#  Question-4:

# Given a Binary Tree, The task is to print the **bottom view** from left to right. A node **x** is there in output if x is the bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal to a horizontal distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

# **Examples:**

# **Input:**

#              20

#            /     \

#         8         22

#     /      \         \

# 5         3        25

#         /    \

#    10       14

# **Output:** 5, 10, 3, 14, 25.





