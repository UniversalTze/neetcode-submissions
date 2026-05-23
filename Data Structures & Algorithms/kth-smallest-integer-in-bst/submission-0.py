# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1th index binary tree
        # recursive solution
        # binary tree: LHS is lower than root. Know that node furthese towards the left 
        # will always be the smallest in a BST
        # node furthest to the right will largest
        # need a non counter -> keep track of smallest to largest element

        # what you will do: 
        # do a recursive dfs on LHS side of tree to find the smallest element
        # the parent of that node will always be second and then if right child exists then that would be third.
        # how the counter increments
        # if counter == k (return)
        # or do an in order traversal to get array in sorted order

        arr = []
        def inordertraversal(root, arr):
            if root is None:
                return
            inordertraversal(root.left, arr)
            arr.append(root.val)
            inordertraversal(root.right, arr)
            return arr
        

        sortedarr = inordertraversal(root, arr)
        return sortedarr[k - 1]


            
        