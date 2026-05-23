class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charSeen = {}
        maximum = 0
        for index in range(len(s)):
            if s[index] not in charSeen:
                charSeen[s[index]] = 1
                maximum = max(len(charSeen), maximum)
            else:
                while s[index] in charSeen:
                    # if character has been seen (already exists in dic), 
                    # pop things out off dictionary as we move a pointer up to keep track 
                    # of where the sequences is valid again. 
                    charSeen.pop(s[start])
                    start += 1
                charSeen[s[index]] = 1 # place it in dictionary as character is part of sequence
        return maximum        