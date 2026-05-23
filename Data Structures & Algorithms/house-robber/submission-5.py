class Solution:
    def rob(self, nums: List[int]) -> int:
        # brute force (recursiion): O(2^N) as checking all possibilities of all subarrays
        # from N, its [N+2:]
        # or [N+1:]
        # at each stage you make two choices rob current house and skip next house
        # skip this house and move to next house
        # recursion takes each path into consideration. 
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            money = max(nums[i] + dfs(i+2), dfs(i + 1))
            memo[i] = money
            return memo[i]

        return dfs(0)
        