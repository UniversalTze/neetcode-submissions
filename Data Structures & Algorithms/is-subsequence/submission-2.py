class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): 
            return False

        if len(s) == 0:
            return True
        currentCount = 0
        for index in range(len(t)):
            if s[currentCount] == t[index]:
                currentCount += 1
            if currentCount == len(s):
                return True
        return False
            
            
        