# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # thinking using ranges,
        # For node.left children, the range that is modified is the upper range
        # this is because all values to the left should be less than its parent node, 
        # making the current node's val the largest value if a left child exists. 

        # For node.right
        # All values to the right must be larger than the current node. Thus the current node,
        # becomes the smallest value a node can hold to the right. Thus the lower range is made to be
        # the current node

        def dfs(node, lower, upper):
            if node is None:
                return True
            # if not satisfied this range then tree is invalid
            if not lower < node.val < upper:
                return False
            # everything to the left of the tree must be less than root and its parent
            # everything to the right of the tree must be more than root and its parent
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        # just set ranges to infinity for root node
        return dfs(root, float("-inf"), float("inf"))

            
        