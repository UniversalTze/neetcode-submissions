# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 # used to keep track of maximum diameter


        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left) # get down to most left  oee
            right = dfs(root.right) # get to right most child
            res = max(res, left + right) # update to find diameter
            return 1 + max(left, right)

            # e.g [1,2,3]
            # at 1, left = dfs(2), right = dfs(3)
            # at 2, left = dfs(None), right = dfs(None)
            # dfs None = 0, so at 2, left = 0, right = 0
            # res = max(0 (global), 0 (L + R))
            # dfs(2) returns 1 + max(0,0) = 1
            # so 1, left = 1 (dfs(2)) and right = 1 (followinf steps above))
            # at 1, res = max(0, 1 + 1)
            # which is 2, (returned)
        dfs(root)
        return res







        