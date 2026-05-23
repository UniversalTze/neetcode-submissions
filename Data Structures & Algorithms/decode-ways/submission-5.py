class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: 
            return 1

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
        