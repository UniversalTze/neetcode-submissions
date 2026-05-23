class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            # if it starts with a 0, there is no valid encodings for the string
            return 0
        # if you encounter any where it cannot be encoded, return 0 immediatedly. 
        # these cases occur when 0 is at the start or on the RHS of a number greater than
        # 2
        # store the length of it in as the "goal"
        dp = {}

        def dfs(i):
            # example "121"
            if i == len(s): 
                return 1
            if i in dp:
                # if i == length or a case that has been solved, return that value
                # so that that path does not need to be gone down. 
                # i represents index. 
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
            # 1st iteration will go get all individual number first
            # dfs(1), dfs(2), dfs(3). (3 is the length of the string)
            # At the end it is: dp = {3:1,1:1}, i = 2, before it returns res from dfs(3)
            # dfs(2), i = 1, i + 1 = 2 < len(s) and s[1] == "2" and s[i+1] = "1"
            # so it does dfs(1 + 2), which will return 1 to the total so res = 2

            return res

        return dfs(0)

        