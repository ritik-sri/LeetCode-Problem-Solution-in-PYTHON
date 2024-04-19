import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min heap
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            # If the size of the heap exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The top of the heap will be the kth largest element
        return min_heap[0]
