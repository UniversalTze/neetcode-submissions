class Solution:
    def hammingWeight(self, n: int) -> int:
        #result = n & 1 this just does it for 00000001 and N, which just returns 1
        # what is needed to be down is remove the LSB
        # to remove LSB, do an AND with the number that came before it
        # e.g 3 = 11 and 2 is 10 (thus, removing the LSB if you an AND)
        # same for: 2 = 10, 1 = 01 (2(10) & 1(01) = 00) 

        # a better example is: 
        # 12 = 1100, the LSB here is the second slot
        # 11 = 1011, where the LSB will be removed when doing and AND. Keep going until 
        # all 1's has been removed, while keeping a counter each time this operation happens
        # the counter is will represent how many 1 bits is in given number
        
        # In computer science theory, a single bitwise operation like & is considered O(1) if 
        # the numbers fit into a standard CPU register (typically 32 or 64 bits).
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
        
        