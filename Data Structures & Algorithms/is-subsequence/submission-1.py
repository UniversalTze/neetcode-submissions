class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s) or len(s) == 0: 
            return False
        currentCount = 0
        for index in range(len(t)):
            if s[currentCount] == t[index]:
                currentCount += 1
            if currentCount == len(s):
                return True
        return False
            
            
        