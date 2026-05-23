class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a fast and slow pointer to detect the largest window. 
        # for a character we haven't seen slide the slow pointer up
        # fast pointer continues to move forward
        # if pointer 
        # hash required
        seenChars = set()
        slow = 0
        counter = 1 # lowest it can always be
        if len(s) == 0: 
            return 0
        seenChars.add(s[slow]) # add first letter of string to seen set.

        for index in range(1, len(s)): 
            # use i index as the window
            if s[index] not in seenChars: 
                seenChars.add(s[index]) # add seen characters to a seen set 
                counter = max(counter, index - slow + 1) # store the largest window
            else:
                # need to add one here as that is how charactering indexing works to include the nth character.
                # if current character is either in seen set or slow character = fast character 
                while s[slow] != s[index]:
                    seenChars.remove(s[slow]) # remove characters in window as they no longer count
                    slow += 1
                if s[slow] == s[index]:
                    slow += 1
                counter = max(counter, index - slow + 1)

        return counter

        