class MedianFinder:

    def __init__(self):
      
        self.small: list[int] = []    # max-heap (negated) — lower half
        self.large: list[int] = []
        

    def addNum(self, num: int) -> None:
        # Step 1: always push to small (max-heap of lower half)
        heapq.heappush(self.small, -num)

        # Step 2: ensure ordering invariant: max(small) <= min(large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: rebalance sizes — keep small ≥ large, difference ≤ 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])               # odd total: middle element
        return (-self.small[0] + self.large[0]) / 2.0
        