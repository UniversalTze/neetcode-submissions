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
            # nodes can be equal too. (edge case)
            # if one node is equal to current root of subtree, it is the highest descendant 
            # as any child after it cannot be a current descendant of it. Thus that's why an equal is used in both conditions
            # This is the same for when left and right child diverges in direction in BST. 
            # any left/right child node cannot be a descendant of the other. Only the node 
            # where p goes down left/(right) and q goes down right/(left) can be a descendant of both. 
            if p.val <= node.val and q.val >= node.val: 
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
            if p.val > node.val and q.val > node.val:  # optimised
                return findLowestAncestor(node.right)
            else:
                return findLowestAncestor(node.left)
            
            
        return findLowestAncestor(root)

            


            

        
        