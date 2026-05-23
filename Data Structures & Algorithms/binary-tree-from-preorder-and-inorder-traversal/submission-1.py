# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        This is probably not needed.
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0]) # or inorder (doesn't matter)
        # the first node of the preorder is always the root
        
        # build hashmap of nodes and their position in the inorder array
        indices = {val: idx for idx, val in enumerate(inorder)} 

        if not preorder or not inorder:
            return
        node = TreeNode(preorder[0]) # root node
        # the inorder array can be used to seperate what is left and right of the root and the parent of subtree
        # everything to left of it, belongs to LHS and everything to the right belongs to the right. 
        # Inorder and preorder lengths are the same
        # use a set to track what has been seen and we'll need two indexes. One for preorder and the order inorder
        index = 0
        while index < len(inorder) and inorder[index] != node.val:
            index += 1
        node.left = self.buildTree(preorder[1:index + 1], inorder[1:index+1])
        node.right = self.buildTree(preorder[index + 1:len(preorder)], inorder[index + 1: len(inorder)])
        return node
        # this question uses sub arrays so can just use this initial function
        """
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
        

            
