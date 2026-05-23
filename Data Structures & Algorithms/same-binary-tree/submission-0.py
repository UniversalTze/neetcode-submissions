# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if a tree is the same 
        # recursively move down each tree checking each node
        # check if left and right down at each node is the same

        if p is None and q is None: # bottom of the tree
            return True
        if p is None and q or q is None and p or p.val != q.val:
            return False
        # left first, now need to check right
        check1 = p.left
        check2 = q.left
        res = self.isSameTree(check1, check2)
        if res:
            # how to do right
            check1 = p.right
            check2 = q.right
            res = self.isSameTree(check1, check2)

        return res
        


        
                
        
        