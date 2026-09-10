class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        spoint = 0
        tpoint = 0
        while spoint < len(s) and tpoint < len(t):
            if s[spoint] == t[tpoint]:
                tpoint += 1
            spoint += 1

        if tpoint == len(t):
            # entire sub string been found, so return 0
            return 0
        else:
            return (len(t) - tpoint)
        

        