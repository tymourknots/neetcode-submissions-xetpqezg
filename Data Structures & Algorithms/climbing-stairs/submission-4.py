class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(1, n):
            temp = one + two
            one = two
            two = temp
        
        return two