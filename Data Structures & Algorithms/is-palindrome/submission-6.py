class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: # flipping it forwards and backwards for length of 1 doesn't matter
            return True
        clean = s.strip(' ')
        clean = clean.replace(" ", '')
        filtered = ""
        for char in clean: 
            if ord(char) >= ord('a') and ord(char) <= ord('z'):
                filtered += char
            elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
                filtered += chr(ord(char) - (ord('A') - ord('a')))
            elif ord(char) >= ord('0') and ord(char) <= ord('9'):
                filtered += char

        start = 0
        end = len(filtered) - 1
            
        while (start <= end): 
            if filtered[start] != filtered[end]: 
                return False
            start += 1
            end -= 1
        return True  