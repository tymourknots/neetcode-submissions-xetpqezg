class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 0

        while left <= right:
            k = (left + right) // 2 
            total = 0

            for pile in piles:
                total += math.ceil(pile / k)
            
            if total <= h:
                res = k
                right = k - 1
            
            else:
                left = k + 1
        return res

    




        