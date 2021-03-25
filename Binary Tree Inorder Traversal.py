# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result