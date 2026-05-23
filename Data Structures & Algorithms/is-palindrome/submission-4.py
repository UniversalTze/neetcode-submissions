class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Do it with O(1) space 
        left = 0 
        right = len(s) - 1

        while (left < right): 
            while left < right and not self.is_alpha_num(s[left]): 
                left += 1 # move it along if not a normal aplhabet character
            while right > left and not self.is_alpha_num(s[right]): 
                right -= 1 # move it along if not a normal aplhabet character
            if (s[left].lower() != s[right].lower()): 
                return False
            left += 1 
            right -= 1
            
        return True

    def is_alpha_num(self, c: chr): 
        if ((ord('A') <= ord(c) <= ord('Z')) or 
            (ord('0') <= ord(c) <= ord('9')) or
            (ord('a') <= ord(c) <= ord('z')  )): 
            return True
        return False
        