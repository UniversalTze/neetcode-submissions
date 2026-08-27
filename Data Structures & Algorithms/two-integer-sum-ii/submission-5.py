class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        # idea 
        # o(N) time and O(1) space
        start = 0
        end = len(numbers) - 1

        # ordered list
        while start < end: 
            # since we know its an ordered list -> use two pointer approach based on some arithmetic
            # guaranteed at least one
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            
            # [3, 4, 5, 7] = 9
            # ordered array gives us an advantage: can tell which direction too move depending on arithmetic
            # index pointers start at 3 and 7. 3 + 7 is above target so move end pointer back to 5
            # 3 + 5 < 9, so need to move start pointer up to the next element (4).
            # now 4 + 5 == 9!
            
            # case 1: if sum of start and end is > target, our current sum is too large
            # so we need to reduce it by moving end pointer back by 1 (decrease end value).

            # case 2: if our current sum is below the target (too short) we can increment
            # the start pointer up to the next increasing number
            if numbers[start] + numbers[end] > target: 
                end -= 1
            else: 
                start += 1
            
        return [-1] # not possible here as there is always one solution in array

        