class Solution:
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        count = 0
        # idea was to use a heap, but that won't work with negative numbers
        # idea of queue was correct. 
        # unless I was to implement a max heap myself
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output


        