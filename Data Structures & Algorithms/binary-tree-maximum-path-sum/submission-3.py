# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # what we know from previous problems is that greedy will not work here 
        # when picking a path. However, the value will be reset if it goes 0 as 
        # negative numbers don't contribute to maximu value
        maximum = float("-inf") # negative infinity, just incase any the entire is negative
        count = 0
        #nodesSeen = set()
        # maybe a bottom up approach is better? correct
        # now parse left and right subtree before going back up to current node 
        # that is where I'm currently going wrong
        # as the nodes can only be apart of the sequence, we can only select two paths 
        # at the root. 

        def maxSumPath(node):
            nonlocal maximum
            nonlocal count
            #nonlocal nodesSeen
            if node is None: # base case
                return 0
            left = maxSumPath(node.left)
            right = maxSumPath(node.right)
            print(right)
            print(left)
            
            if left + right + node.val >= maximum:
                count = left + right + node.val
                #print(count)
            else: 
                count = left + right + node.val
            maximum = max(count, maximum)
            minedge = min(left, right)
            count -= minedge
            #nodesSeen.add(node)
            #maximum = max(count, maximum)
            if count < 0:
                count = 0
            
            return count
        maxSumPath(root)
        return maximum

        