class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)
        if len(stones) > 0:
            return abs(stones[0])
        else:
            return 0