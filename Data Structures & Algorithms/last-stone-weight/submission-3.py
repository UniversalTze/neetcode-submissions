import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index in range(len(stones)):
            stones[index] = -(stones[index])

        # convert stones to a min heap (default using heapq.heapify)
        heapq.heapify(stones)
        while len(stones) > 1:
            val1 = abs(heapq.heappop(stones))
            val2 = abs(heapq.heappop(stones))
            diff = val1 - val2
            heapq.heappush(stones, -diff) 

        return abs(heapq.heappop(stones))

        