class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of what has been seen. 
        # when you get to a duplicate, start 
        # removing items from the set, until character, 
        # has been removed. 

        # need to keep track of index that you stop at.

        seen = set()
        longest = 0
        stopIndex = 0
        for index in range(len(s)):
            if s[index] not in seen:
                seen.add(s[index])
            # if character has been seen don't add to the set just yet
            else:
                while s[index] in seen:
                    seen.remove(s[stopIndex])
                    stopIndex += 1
                # remove everything until duplicate is removed
                # now add current element to the set
                seen.add(s[index])
            
            longest = max(len(seen), longest)

        return longest