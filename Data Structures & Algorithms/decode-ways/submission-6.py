class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: 
            return 1
        # Recurrence to solving this:
        # prev = CurIndex - 1
        # Combinations[CurIndex] = 
        # If CurIndex > 0 then use dp[CurIndex - 1] + 
        # If prev == 1 and CurIndex in "0123456789" or 
        # prev = 2 and CurIndex in "123456"
        # then its valid to use dp[CurIndex - 2]
        
        # Two cases
        # 1st
        # If current index valid by itself, it can use the number of decoded ways 
        # found in CurIndex - 1
        
        # 2nd
        # As 10-26 map to valid characters, need to check if the index before cur index is a 
        # 1 or 2 and that current index fits inbetween the required bounbaries. E.g 29 is out
        # 26 is within boundary. The number of valid combinations that can be found if valid 
        # is at CurIndex - 2

        # Example: 126
        # dp = [-1,-1,-1,-1], set initial params: dp = [1,1,-1,-1]
        # start at index 1, which is 2. 2 is valid, so use index 1. 
        # 12 is also valid (prev = 1), so use index - 1 = 0
        # dp[index + 1 (2)] = 1 + 1
        # so dp = [1,1,2,-1]

        # now check 6, index = 2, p = [1,1,2,-1]
        # 12,6 (for visual) 6 is valid so use dp[index] = 2
        # 1,26 (for visual) 26 is also a valid combo, so the combinations at 1's index (which is 1 in dp)
        # is valid. dp[index - 1] = 1
        # dp[index + 1 (3)] = 2 + 1
        # so dp = [1,1,2,3]
        # dp[nums] = 3 is returned. 
        # decode ways: 126 = 1,2,6 | 12,6 | 1,26

        dp = [-1] * (len(s) + 1)
        dp[0] = 1 # this represents empty string and there to handle empty string
        # no input = no output, which counts as 1 decoding

        # for any digits 1-9 put 1 else 0 
        if s[0] == "0":
            # first character in string is second index of dp. 
            dp[1] = 0
        else:
            dp[1] = 1
        # set the first two indexes
        for index in range(1, len(s)):
            # loop from 1 to len(s)
            # keep in mind that indexing into dp and updating it
            # is index + 1 as we have a zero index for empty strings in dp.
            # Index begins from 1, as we've already checked the 0th index (first one) of the string

            # therefore index into normal string is normal. 
            # Indexing into DP Array is index + 1. e.g 1st of string would be represented properly in the
            # 2nd index for DP. (Holding combinations for decoding string)
            # this means if we were using current index, into dp, it would actually be using index - 1 values
            decodeWays = 0
            check = s[index]
            if check != "0":
                # this index into dp represents number of ways to decode up to index - 1.
                decodeWays = dp[index]
            # check the previous character
            # we can use index - 2 if it the number is inbetween 10 and 26.
            prev = s[index - 1]
        
            if prev == "1" and check in "0123456789" or prev == "2" and check in "0123456":
                decodeWays += dp[index - 1]
            dp[index + 1] = decodeWays
        return dp[len(s)]
        