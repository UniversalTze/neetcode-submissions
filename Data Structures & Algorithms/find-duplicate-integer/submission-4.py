class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use arithmetic sequence
        # and nums contains at least n + 1
        # only work if sequence is like 1 + 2 + 3 ..... (not the case)

        # Linked List Cycle Problem
        # Floyd's Algo (beginning of the linked list)
        # think of the numbers as pointers to the next pointer in linked list
        # [1,3,4,2,2]
        # index 0 points to index 3, 3 points to index 2, 2 points to 4 and so on....

        # index 0 is not included as the range of items in the array are [1, N]

        """
        How Floyd's algo works: 
        Use a fast and slow pointer, fast jumps 2, slow jumps 1. After doing this,
        your code will get to an intersection where fast == slow (same index)

        Then use another slow pointer at the start and use the current slow pointer
        and move them by one until you they meet at the same node. This is the entrace of the
        cycle. 

        Intuition: The first intersection betweem fast and slow pointer will always
        be the same distance from the start to the entrance of the cycle (main idea of algo)

        Math:
        2 * slow = Fast
        p represents distance from begin to start of cycle
        C represents cyle
        X represents the distance to beginning of cycle to intersection between fast and slow
        C - X is the part of the cycle minus the distance of intersection to beginning of cycle

        Fast = P + C - X + C = P + 2C - X
        Slow = 2(P + C - X) = 2P + 2C - 2X
        = -P + X = P - X = 0  P = X
        (proof)
        The beginning of the cycle is returned! (is the indexed duplicate number)
        """

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow # beginning of the cyle (return value we're looking for)

        