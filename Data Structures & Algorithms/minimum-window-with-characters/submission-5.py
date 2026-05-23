class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            # no substring occurs as length S is shorter than T
            return ""

        # as upper and lower case chracters are allowed. 
        # from the examples, assume that upper case characters associate with uppercase
        # and lower case associated with lower case.
        
        # as order does not matter, need to use frequency of count (Map or array)
        # keep count and index? when the three has been found
        
        # use a hashmap so no need for calculating character arrays
        # edge case -> need to store the last n items if next to each other
        # else just the last item that was popped off.
        result = ""
        counter = 0
        substringCount = {}
        for char in t: 
            if char not in substringCount: 
                substringCount[char] = 1
            else: 
                substringCount[char] += 1

        # redo without a copy
        # idea have a dynamic window that slides out first to find a valid window
        # then slide it that the LHS of windos until its no longer satisfied. 
        # When its this case, slide the RHS of window until condition is satisfied

        # whilst doing this keep a length of substring. (could do by subtracting indexes)
        # use states (valid state for removing strings)
        start = 0 # starting index of substring in normal string
        shortestStart = 0
        shortestEnd = 0
        length = -1
        found = False
        normalcount = {}
        for index in range(len(s)): 
            # loop through S and do the check
            if s[index] in substringCount:
                if s[index] not in normalcount:
                    normalcount[s[index]] = 1 # adds a count to the normal count mapping
                else:
                    normalcount[s[index]] += 1 # increment a counter
                
                if normalcount[s[index]] == substringCount[s[index]]: # do == instead of >=
                    # use a counter instead of mapping over a map looking the counts each time
                    # becomes O(1) average instead of O(N) time
                    # smarter way to query a map and keep track of counter
                    # if character count matches increment counter for that specific character
                    # if counter matches the substringCount items length (a substring exists)
                    counter += 1
            # if counter is true for all characters in string then enter this if block
            if counter == len(substringCount):  # found a substring in the string
                found = True # there exists a substring t in s. (indicate that)
                # index is the end of the substring
                while start <= index:
                    # start shrinking the window (find minimum)
                    if s[start] in substringCount:
                        normalcount[s[start]] -= 1
                        if normalcount[s[start]] < substringCount[s[start]]:
                            counter -= 1 # decrement counter as its no longer part of the window
                    start += 1 # increment start forward no matter what 
                    # This means that start pointer will always be the index after the character that completes
                    # the substring has been removed.
                    # thus, subsequent operations with start need to decrement count by 1

                    # e.g s = "ab", t = "b"
                    # start will be at the pointer after "b", where index is pointing to "b". (problem if indexing using start)
                    # but what we do is always decrement start by 1, so that the character apart of substring is till 
                    # in window
                    # start begins at 0. "a" so -> start is now 1
                    # start = b, decrements count from normalcount and counter so counter != len(substringCount) no longer true.
                    # start is still incremented by 1, so start = 2.
                    # index = 1, and start = 2 (decrement), so starting index = 1. 
                    if counter != len(substringCount):
                        break

                # current position of start is 1 + prev character index that had the substring in the string
                # so we need to subtract 1 from start. (calculate length)
                checklen = index - (start - 1) + 1
                if length == -1 or checklen < length:
                    length = checklen
                    shortestStart = start - 1 if start > 0 else 0 # subtract 1 from start when setting it to shortest start
                    shortestEnd = index # index represents the current character where a substring has been formed
                    # so need to add 1 when including it in the range. 
        if found:
            for char in range(shortestStart, shortestEnd + 1): 
                result += s[char]

        return result