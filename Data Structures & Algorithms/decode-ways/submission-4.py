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
            decodeWays = 0
            check = s[index]
            if check != "0":
                decodeWays = dp[index]
            prev = s[index - 1]
            if prev == "1" and check in "0123456789" or prev == "2" and check in "0123456":
                decodeWays += dp[index - 1]
            dp[index + 1] = decodeWays
        return dp[len(s)]
        