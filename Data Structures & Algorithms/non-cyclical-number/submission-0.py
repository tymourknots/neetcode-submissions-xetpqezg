class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sum(n)

            if n == 1:
                return True
        return False
    
    def sum(self, n):
        res = 0

        while n:
            digit = (n % 10) ** 2
            res += digit
            n = n // 10
        return res
            