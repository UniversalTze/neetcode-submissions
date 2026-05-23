class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # order does not matter, only frequency of characters as permutation
        if (len(s1)) > len(s2):  # no substring can occur of this happens
            return False
        ALPHABET = 26

        # initialise an array counter array (each index is a frequency counter)
        checkS1 = [0] * ALPHABET
        checkS2 = [0] * ALPHABET

        for index in range(len(s1)):
            checkS1[ord(s1[index]) - ord('a')] += 1
            checkS2[ord(s2[index]) - ord('a')] += 1
        # create an initial sliding window into S2 
        print(checkS2)
        l, r = 0, len(s1) - 1 
        while r < len(s2): 
            print(r)
            # same pattern of lenght S1 has been found (a permutation of substring)
            if checkS1 == checkS2: return True

            checkS2[ord(s2[l]) - ord('a')] -= 1 # remove a frequency from a character (out of window)
            l += 1  
            r += 1
            if r == len(s2): continue
            print(r)
            checkS2[ord(s2[r]) - ord('a')] += 1  

        return False
        