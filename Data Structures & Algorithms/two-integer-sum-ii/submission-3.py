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
            # 
            if numbers[start] + numbers[end] > target: 
                end -= 1
            else: 
                start += 1
            
        return [-1]

        