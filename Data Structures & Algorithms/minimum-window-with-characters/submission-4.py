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
                if s[index] not in normalcount: # something wrong this this logic (need to do a test first before adding)
                    normalcount[s[index]] = 1
                else:
                    normalcount[s[index]] += 1
                
                if normalcount[s[index]] == substringCount[s[index]]: # do == instead of >=
                    counter += 1
            if counter == len(substringCount):  # found a substring in the string
                found = True # there exists a substring t in s
                # index is the end of the substring
                while start <= index:
                    # start shrinking the window (find minimum)
                    if s[start] in substringCount:
                        normalcount[s[start]] -= 1
                        if normalcount[s[start]] < substringCount[s[start]]:
                            counter -= 1
                    start += 1
                    if counter != len(substringCount):
                        #print(start)
                        break
                # current position of start is 1 + prev character that had the substring in the string
                #print(index)
                checklen = index - (start - 1) + 1
                print(checklen)
                if length == -1 or checklen < length:
                    length = checklen
                    shortestStart = start - 1 if start > 0 else 0
                    shortestEnd = index
        if found:
            for char in range(shortestStart, shortestEnd + 1): 
                result += s[char]
        #print(shortestStart)
        #print(shortestEnd)
        return result