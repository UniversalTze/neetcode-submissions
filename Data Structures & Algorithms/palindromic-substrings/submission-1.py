class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for index in range(len(s)):
            count += 1 # this will all single characters
            # as these subtring single characters are palindromes
            i,j = index - 1, index + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                # odd case palindrome
                # idea is that every index is treated as the centre of the palindrome
                count += 1
                i -= 1
                j += 1
            
            i,j = index, index + 1 # even case
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            
        return count
        