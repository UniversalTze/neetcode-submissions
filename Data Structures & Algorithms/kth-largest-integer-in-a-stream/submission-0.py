import copy, heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create a min heap and pop it off the list 
        # so add is a O(1) constant operation as we create a copy and just 
        # pop twice to get the max.
        self.order = k
        self.heap = nums
        self.length = len(nums)
        heapq.heapify(self.heap) # O(N) operation       

    def add(self, val: int) -> int:
        self.length += 1
        heapq.heappush(self.heap, val)
        copied = copy.deepcopy(self.heap)
        for index in range(self.length - self.order):
            heapq.heappop(copied)
        # head of copied should be the kth largest element (multipled by -1 to get back its original value)
        return copied[0]


        
