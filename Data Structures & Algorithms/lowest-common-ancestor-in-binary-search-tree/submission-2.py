# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findLowestAncestor(node):
            # from this we know that two nodes are on the same side from root.
            # idea is bottom is better than top down
            # recurse down to leaf trying to find p or q
            # know that lowest common ancestor occurs when a split occurs. 
            # we know a split occurs as we in BST, where if both nodes are less than current node we're checking
            # they exist in the same side of subtree. (more than case is not needed)
            if not node:
                return
            if p.val <= node.val and q.val >= node.val: # nodes can be equal too
                return node
            if p.val >= node.val and q.val <= node.val:
                return node
            """
            They're looking for lowest as in node closest with the highest depth, farthese away from root 
            and closest ancestor to the child nodes. 
            
            if p.val > node.val and q.val > node.val: # ahhh this is incorrect
                # root will always be a descendant of every node, so if both p and q are larger than root
                # root can be returned.  (or current node that is root of a subtree)
                return node
            """
            return findLowestAncestor(node.left) or findLowestAncestor(node.right)
            
            
        return findLowestAncestor(root)

            


            

        
        