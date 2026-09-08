class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for index in range(1, len(s)):
            prev = s[index - 1]
            prevval = ord(prev)
            curval = ord(s[index])
            score += abs(prevval - curval)
        return score