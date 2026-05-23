class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) time and O(N) space

        # convert numbers into a hashset 
        num_set = set(nums)

        # begininning of a sequence: 
        # If n - 1 does not exist in array, indicates beginning of sequence
        longest = 0
        for num in nums: # this solution won't work as we are resetting count
            if num - 1 not in num_set: 
                length = 0
                while num + length in num_set: 
                    length += 1
                longest = max(length, longest)

        # Visit each number in the array twice -> once to check if its a beginning of a sequence
        # and second time is if it is apart of the sequence. 
        # That is how it is done optimally rather than checking if current number is a sequence. 

        return longest
            


        