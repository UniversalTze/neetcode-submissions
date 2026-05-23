class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) time and O(N) space
        # convert a list to a hash set 
        # set holds all distinct numbers in the set
        numSet = set(nums)
        seen = set()

        # a consecutive sequence begins when there is no left neighbour (number smaller than 1 to the left)
        # only check when a sequence begisn else no check needed
        longest = 0
        for num in nums: 
            if num - 1 not in numSet: 
                if num in seen: # for optimisation so no repeated sequences need to be done again
                    continue
                # no left neighbour, we know its the beginning of a sequence
                length = 0
                checkNum = num
                while checkNum in numSet: 
                    length += 1
                    checkNum += 1

                longest = max(length, longest)
                seen.add(num)
        return longest