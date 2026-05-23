class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor property
        # doing xor twice with the same value will cancel the values out and return you to original value
        # If you xor two of the same values, it will cancel itself out returning 0. Xor 0 with a number keeps the 
        # number you XOR 0 with. 
        res = 0
        for num in nums:
            res = res ^ num
        return res