class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            fart = 0
            for i in range(left, right + 1):
                fart = max(fart, i + nums[i])
            left = right + 1
            right = fart
            res += 1
        return res