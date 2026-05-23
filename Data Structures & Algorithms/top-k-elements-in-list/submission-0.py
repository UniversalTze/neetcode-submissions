import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:  # only 1 item in K, return that
            return [nums[0]]

        # Create an empty list to represent the heap 
        # use a map to keep track of count and place count and element into tuple

        seen = {}
        for num in nums: 
            if num in seen: 
                seen[num] = seen.get(num) + 1
            else: 
                seen[num] = 1

        # use a heap to store maximum based on count
        # python uses a min heap automatically so to mimic it to be a max heap 
        # make numbers negative.
        heap = []
        for key, value in seen.items(): 
            heapq.heappush(heap, (-value, key))
        # resulting array
        result = []
        for i in range(k): 
            value, key = heapq.heappop(heap)
            result.append(key)

        
        return result



        