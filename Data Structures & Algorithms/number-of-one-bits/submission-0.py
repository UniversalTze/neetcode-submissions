class Solution:
    def hammingWeight(self, n: int) -> int:
        #result = n & 1 this just does it for 00000001 and N, which just returns 1
        # what is needed to be down is remove the LSB
        # to remove LSB, do an AND with the number that came before it
        # e.g 3 = 11 and 2 is 10 (thus, removing the LSB if you an AND)
        # same for: 2 = 10, 1 = 01 (2(10) & 1(01) = 00) 
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
        
        