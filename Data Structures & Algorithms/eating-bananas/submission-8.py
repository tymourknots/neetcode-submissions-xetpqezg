class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxF = max(piles)
        minK = maxF

        left = 1
        right = maxF

        while left <= right:
            total = 0
            k = (left + right) // 2
            for pile in piles:
                total += math.ceil(pile / k)
            if total <= h:
                minK = min(minK, k)
                right = k - 1
            else:
                left = k + 1
        return minK