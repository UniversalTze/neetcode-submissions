from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # try a monotonic queue: 
        queue = deque()
        output = []
        # push index and position onto queue
        for index in range(len(nums)):
            if not queue:
                queue.append((nums[index], index))
            elif nums[index] <= queue[-1][0]:
                queue.append((nums[index], index))
            elif nums[index] > queue[-1][0]:
                while queue and nums[index] > queue[-1][0]:
                    queue.pop()
                queue.append((nums[index], index))
            if index >= k - 1:
                if queue[0][1] <= index - k:
                    queue.popleft()
                output.append(queue[0][0])

        # monotic queue (decreasing order so start of queue has highest number)
        return output

        
        