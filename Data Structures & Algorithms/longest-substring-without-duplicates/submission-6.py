class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charSeen = set()
        maximum = 0
        for index in range(len(s)):
            if s[index] not in charSeen:
                charSeen.add(s[index])
                maximum = max(len(charSeen), maximum)
            else:
                while s[index] in charSeen:
                    # if character has been seen (already exists in dic), 
                    # pop things out off dictionary as we move a pointer up to keep track 
                    # of where the sequences is valid again. 
                    charSeen.remove(s[start])
                    start += 1
                # After removing the old index of current character from the string, you need to add this new index to 
                # the hash map

                # note that this index doesn't really do an
                charSeen.add(s[index])
        return maximum        