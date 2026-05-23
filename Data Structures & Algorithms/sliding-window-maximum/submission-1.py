class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # idea was to use a heap, but that won't work with negative numbers
        # idea of queue was correct. 
        # heap is not optimal tho, using a montonic queue is. 
        heap = []
        output = []
        for i in range(len(nums)):
            # push number and current index onto heap
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                # for any index above k - 1, use top of the heap, but need to 
                # check bounds
                # if index of max heap no longer in window, pop until there is an option in the window
                while heap[0][1] <= i - k:
                    # this calculates min value index given the window
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        # time complexity is O(N * Log(N)) to build the heap and to search for node to remove. 
        return output


        