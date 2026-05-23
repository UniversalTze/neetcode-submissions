class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # new idea is to use pre and post and find maximum of both
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
        print(pre)
        print(post)
        maximum = float("-inf")
        for i in range(NUMS_LENGTH):
            maximum = max(maximum, post[i], pre[i])
        return maximum

            
        