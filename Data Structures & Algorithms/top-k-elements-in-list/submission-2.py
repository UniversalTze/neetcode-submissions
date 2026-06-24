class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # other solutions: Hash or bucket sort

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

        # building a heap is O(log n) for each n, there needs to be log n 
        # pushes down the tree
        """
        heap = []
        for key, value in seen.items(): 
            heapq.heappush(heap, (-value, key))
        # resulting array
        result = []
        for i in range(k): 
            value, key = heapq.heappop(heap)
            result.append(key)
        """
        # create a bucket for bucket sort. 
        # Each index represent a count, within each index will be a list of numbers
        buckets = [[] for i in range(len(nums) + 1)] 

        for key, value in seen.items(): 
            buckets[value].append(key)

        result = []
        # no need for 0th index of buckets
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                if len(result) == k: 
                    break
                result.append(n)
                

        return result        
        