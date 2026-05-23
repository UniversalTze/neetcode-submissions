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

        """
        explanation:
        Bottom up approach is sort of a DP approach where subproblems are solved. This only takes O(N) time and O(H)
        where N is the n number of nodes, and H is the height of the tree. Worst case for space is N. 
        
        Since I use a bottom up approach, it will start from the leaf nodes and work its way up. 
        The idea at each node, it tests the maximum by being the "root" of the maximum subtree. This means
        that both maximum of both Left and Right along with current node being "root" added to a count variable.
        If its larger than current maximum, replace it. Else, we find the minimum edge value between left and right, and 
        subtract it from the current count. So that when it returns the count to the parent (Left or right), it has taken 
        only the pathway Left or right, so that the parent can now tested as the "root" where Left and Right edges can be accounted 
        for in the total. 

        What I realised was that, since a node can not appear in the sequence more than once, only the "root" of the max subtree 
        can take a left and right path. 

        This also negative numbers, if the current is below 0, its just gets reset to 0 as negative numbers
        don't help achieve the max value of the subtree. 
        """
        def maxSumPath(node):
            nonlocal maximum
            nonlocal count
            #nonlocal nodesSeen
            if node is None: # base case
                return 0
            left = maxSumPath(node.left)
            right = maxSumPath(node.right)

            count = left + right + node.val
            """
            if left + right + node.val >= maximum:
                count = left + right + node.val
                #print(count)
            else: 
                count = left + right + node.val
            """
            maximum = max(count, maximum)
            minedge = min(left, right)
            count -= minedge
            if count < 0:
                count = 0
            
            return count
        maxSumPath(root)
        return maximum

        