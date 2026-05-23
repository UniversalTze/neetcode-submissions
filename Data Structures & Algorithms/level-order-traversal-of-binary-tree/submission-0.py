# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use a map and also for each level -> use a non local or can pass level
        # but use a non local map
        if not root:
            return []
        nodeLevel = {}
        level = 0  # current root level/depth
        # have a seperate function for dfs and level
        # create the function here so that it has a the outer scope (nodelevel map)
        def dfs(root, level):
            nonlocal nodeLevel
            if not root: 
                return level # incremented an extra level that was not needed (used for range so it works out with that extra level)
            if level not in nodeLevel:  # store the nodes at each level in a map that be queried O(1) after map has been made
                nodeLevel[level] = [root.val]
            else: 
                add = nodeLevel[level]
                add.append(root.val)
                nodeLevel[level] = add
            left = dfs(root.left, level + 1) # returned level heights
            right = dfs(root.right, level + 1)
            return max(left, right) # keep track of max level, used to iterate through map in an ordered manner
        maxLevel = dfs(root, level)

        result = []
        for level in range(maxLevel):
            result.append(nodeLevel[level])
        return result

        