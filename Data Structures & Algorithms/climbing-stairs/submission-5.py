class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-2, -1, -1):
            temp = one + two
            one = two
            two = temp
        
        return two