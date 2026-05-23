class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # another way to do this without the extra space. 
        """
        Kadane Algo:
        (General)
        The algorithm iterates through the array once, keeping track of two main variables: 
            current_sum: The maximum sum of a subarray ending at the current position.
            max_sum: The overall maximum sum found so far across the entire array. 
        At each element, the algorithm decides whether to extend the current subarray or 
        start a new one from the current element. 
        If adding the current element to the current_sum yields a sum less than the current element itself, 
        it means the previous subarray was negatively impacting the total, so it is better to start a new subarray 
        with just the current element. 
        """
        # Idea here is to keep a current maximum but also a current minimum (current minimum is used for the negative numberes)
        maximum = float("-inf")
        res = nums[0]
        curMin = 1
        curMax = 1
        for num in nums:
            tmp = curMax * num
            # if curnum is positive, first is true, 
            # if curMin is negative and so is num and its larger than max, second is true
            # or current number, e.g if num is 0, reset it to num * 1 = num
            curMax = max(num * curMax, num * curMin, num)
            
            # for in min()
            # first is true if curMax is positive and num is negative
            # second is true if curMin is negative and multiplied by positive num 
            # which logically provide the minimum. 
            # third is true for a 0 case. 
            curMin = min(tmp, num * curMin, num)

            res = max(res, curMax)
        return res
        """
        # new idea is to use pre and post array and find maximum of both
        NUMS_LENGTH = len(nums)
        pre = [0] * NUMS_LENGTH
        pre[0] = nums[0]
        for index in range(1, NUMS_LENGTH):
            # nums[index] holds current index
            calc = pre[index - 1] * nums[index]
            if calc == 0 and nums[index] > 0:
                pre[index] = nums[index]
            else:
                pre[index] = calc

        post = [0] * NUMS_LENGTH
        post[NUMS_LENGTH - 1] = nums[NUMS_LENGTH - 1]
        for index in range(NUMS_LENGTH - 2, -1, -1):
            product = post[index + 1] * nums[index]
            if product == 0 and nums[index] > 0:
                post[index] = nums[index]
            else:
                post[index] = product

        maximum = float("-inf")
        for i in range(NUMS_LENGTH):
            maximum = max(maximum, post[i], pre[i])
        return maximum
        """

            
        