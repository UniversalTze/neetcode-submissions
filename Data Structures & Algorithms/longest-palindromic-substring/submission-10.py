class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp computes a n by n table in which only half the table gets filled
        # very intricate solution. 
        # the diagonals represent the palindrome of substrings if exist. 
        # I had the same idea where if length between indexes was greater than 2
        # if what came before it is a palindrome, and current indexes fit palindrome rule, 
        # then it is a palindrome

        # brute force is to check from LHS to RHS and check all possible 
        # substring for a palindrome
        # if len(n) string, 
        # i = 0, number of substrings = n
        # i = 1, n - 1
        # i = 2, n - 2.....
        # n + n - 1 + n - 2 + n - 3 .... + 1 = n(n+1)/2 = O(N^2)
        # this is only all possible substrings, it takes O(N) time to check each 
        # substring, therefore, its takes O(N * N ^ 2) = O(N^3)
        # O(1) space tho

        # Solution idea: 
        # Think of each index as the middle of a palindrome, and go as far out as
        # possible keeping in mind of palindrome rules. If indexes out of bounds or
        # palindrome rules are broken, move on. 
        # This checks entire string so O(N) and it takes O(N) to check if palindrome
        # therefore its O(N * N)
        longindex = 0
        length = 0
        for index in range(len(s)):
            # loop through each string option, with each option being
            # the middle of a palindrome
            
            # for an odd palindrome
            left = index
            right = index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # only way they are a palindrome is thaf if characters next to it are the same
                if length < right - left: 
                    # proper length e.g indexes 9 - 7 is length 3 not 2. 
                    length = right - left
                    longindex = left
                left -= 1
                right += 1
            
            # for even
            left = index
            right = index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if length < right - left: 
                    length = right - left
                    longindex = left
                left -= 1
                right += 1
        return s[longindex:longindex + length + 1]
        