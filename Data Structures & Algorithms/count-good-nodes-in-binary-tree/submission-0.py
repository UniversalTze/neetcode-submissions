# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs through the tree node and save the max value
        count = 1 #
        maxim = root.val # outside of the range

        def dfs(root, maxim):
            nonlocal count
            if root is None:
                return count
            if root.val >= maxim:
                count += 1
                maxim = max(root.val, maxim)
            dfs(root.left, maxim)
            dfs(root.right, maxim)
        dfs(root.left, maxim)
        dfs(root.right, maxim)
        return count 

            
                
            
        