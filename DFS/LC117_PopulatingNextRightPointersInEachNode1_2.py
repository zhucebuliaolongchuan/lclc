"""
116,117 Populating Next Right Pointers in Each Node 1 and 2
Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?
Note:
You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Show Company Tags
Show Tags
Show Similar Problems
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is not None:
            last_layer = [root]
            curr_layer = []
            while len(last_layer) > 0:
                for node in last_layer:
                    if node.left is not None:
                        curr_layer.append(node.left)
                    if node.right is not None:
                        curr_layer.append(node.right)
                for i in range(1, len(last_layer)):
                    last_layer[i - 1].next = last_layer[i]
                last_layer = curr_layer
                curr_layer = []
