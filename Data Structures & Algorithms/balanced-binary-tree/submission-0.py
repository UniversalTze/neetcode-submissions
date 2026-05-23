# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # instead of doing it at root and checking every mode to see if balanced 
        # by checking if subtrees below it is balanced O(N)
        # and having to do that for every node (O(N)) it results in O(N^2)).

        # now we just go throught it from the bottom up, if the previous subtrees are balanced, no 
        # more work is needed at current node, except for calculating heights of what was returned by 
        # prev subtreess.

        def dfs(root):
            # return two things, a bool to keep track if still balanced and height of nkde
            # if false, no checks is needed, else check height
            if not root:
                return [True, 0] # balanced at the leaf nodes as height is 0 and 0  of the left and right cjild
            left, right = dfs(root.left), dfs(root.right)
            # left[0] and right[0] need to be true, as this means botu subtrees of left and right 
            # are currently balanced, if one is found to be false, it will be false for entire tree, 
            # which is why AND is here
            balanced = left[0] and right[0] and abs(left[1] - right[1]) < 2
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

        