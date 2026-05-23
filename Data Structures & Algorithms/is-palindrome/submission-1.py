class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower() #filters out the string and all special characters
        print(s)
        lastLetter = len(s) - 1
        firstLetter = 0
        res = True

        while (firstLetter < len(s)): 
            if (s[firstLetter] != s[lastLetter]): 
                res = False 
                break 
            firstLetter += 1 
            lastLetter -= 1
            
        return res
        
        