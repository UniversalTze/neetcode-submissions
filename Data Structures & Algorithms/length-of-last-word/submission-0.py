class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip()
        wordarr = word.split(' ')
        res = len(wordarr[len(wordarr) - 1])
        return res
        
        