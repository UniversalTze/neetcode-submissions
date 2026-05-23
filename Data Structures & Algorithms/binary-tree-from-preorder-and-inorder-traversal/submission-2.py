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
        """
        # build hashmap of nodes and their position in the inorder array
        # O(N)
        # you have indexes of position it lies in the inorder format
        inOrderMap = {val : index for index, val in enumerate(inorder)}

        # the inorder array can be used to seperate what is left and right of the root 
        # and the parent of subtree
        # everything to left of it, belongs to LHS and everything to the right belongs 
        # to the right. 

        # after splitting you can do the recusion as for the inorder trees, 
        # since we're seperating the array using parent node, 
        index = 0
        def splitBuild(left, right):
            # left and right indicate indexes used to build the tree
            # the parents of the node has been found using Hashnodes
            # We know that first node in preorder is always the parent
            # thus we can increment an index after grabbing it.
            # We know that the separation occurs at the index of root node.
            # Anything to the LHS side of it in Inorder array is for left child
            # of current parent and this the true for RHS. 

            nonlocal inOrderMap 
            nonlocal index
            if left > right: 
                return None
            node = TreeNode(preorder[index]) # grab root/parent
            index += 1
            mid = inOrderMap[node.val]
            node.left = splitBuild(left, mid - 1)
            node.right = splitBuild(mid + 1, right)

            return node
        # inorder or preorder doesn't matter here. Just want the indexes. 
        return splitBuild(0, len(inorder) - 1)

        

            
