import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index in range(len(stones)):
            stones[index] = -(stones[index])
        my_heap = stones
        # convert stones to a min heap (default using heapq.heapify)
        heapq.heapify(my_heap)
        while len(my_heap) != 1:
            val1 = abs(heapq.heappop(my_heap))
            val2 = abs(heapq.heappop(my_heap))
            diff = val1 - val2
            heapq.heappush(my_heap, -diff) 

        return abs(heapq.heappop(my_heap))

        