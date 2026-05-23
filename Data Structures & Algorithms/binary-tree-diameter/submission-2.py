# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # need to know the height of node. At leaves nodes, height is 0
        # also count the edges, so 6 nodes = 5 edges for furthest distance
        # use dfs to find leaf, then build subtress moving back up calculating
        # height of current node. However, there are two different heights that occhrs
        # as there is a left and right child. So need to use maximum height
        # use a non local max to keep up the maximum diameter seen
        # maximum diameter = left height  + right height

        maxim = 0

        def dfs(root):
            # fucntion to recursively iterate through the tree to find leaf,
            # to find height.
            nonlocal maxim # for non local item
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maxim = max(maxim, left + right)
            return 1 + max(left, right)
            # when leaf node, left = dfs(none) = 0, right = dfs(none) = 0
            # at leaf node its returns 1 + max(left, right)
            # this will be represnted as the edge to its parent node (1)
            # this represens the max height to current node

        dfs(root)
        return maxim

            







        