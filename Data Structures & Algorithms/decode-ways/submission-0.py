class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            # if it starts with a 0, there is no valid encodings for the string
            return 0
        # if you encounter any where it cannot be encoded, return 0 immediatedly. 
        # these cases occur when 0 is at the start or on the RHS of a number greater than
        # 2
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

        