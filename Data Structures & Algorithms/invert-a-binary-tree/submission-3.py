# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left) # recursion does DFS down LHS side first

        self.invertTree(root.right) # then does right side. first child of 

        return root
        
        