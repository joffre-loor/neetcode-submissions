# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good=0
        def dfs(currNode, currMax):
            nonlocal good
            if not currNode:
                return
            
            if currNode.val >= currMax:
                good+=1
                print(currNode.val)
            
            currMax = max(currMax, currNode.val)
            dfs(currNode.left, currMax)
            dfs(currNode.right, currMax)
        
        dfs(root, root.val)
        return good