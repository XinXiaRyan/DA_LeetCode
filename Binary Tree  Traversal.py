# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):#non-recursive
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
    def inorderTraversal(self, root):#recursive
        result = []
        if root:
            result = self.inorderTraversal(root.left)
            result.append(root.val)
            result = result +self.inorderTraversal(root.right)
        return result


    def preorderTraversal(self, root):#non-recursive
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return res
    def preorderTraversal(self, root):#recursive
 
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        l = self.preorderTraversal(root.left)
        r = self.preorderTraversal(root.right)
        return [root.val]+l+r
