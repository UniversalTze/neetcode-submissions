# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # for empty set as empty set is subset of all sets
            return True
        if not root: # no more nodes to look at to check if subtree
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, sub) -> bool:
        if not root and not sub:
            return True
        if root and not sub:
            return False
        if sub and not root:
            return False
        if root.val != sub.val:
            return False
        print(root.val)
        return self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right)

        
        