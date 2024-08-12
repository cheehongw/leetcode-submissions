class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # maintain a heap with k items
        # smallest item in heap is the k-th largest

        heapify(nums)
        while (len(nums) > k):
            heappop(nums)
        
        self.upper = nums
        self.k = k


    def add(self, val: int) -> int:
        
        if len(self.upper) < self.k:
            heappush(self.upper, val)
        else:
            if (val >= self.upper[0]):
                heappushpop(self.upper, val)


        return self.upper[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
