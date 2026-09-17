class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip()
        res = 0
        for index in range(len(word) - 1, -1, -1):
            if word[index] == " ":
                break
            res += 1
        return res
        
        