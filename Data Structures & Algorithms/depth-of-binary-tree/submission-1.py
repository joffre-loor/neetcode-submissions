# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def deep(depth, root):
            if root is None:
                return depth
            depth+=1
            length_one = deep(depth, root.right)
            length_two = deep(depth, root.left)
            return max(length_one, length_two)
        return deep(depth,root)