class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                res = min(res, nums[left])
            if nums[mid] >= nums[left]:
                left = mid + 1
                res = min(res, nums[mid])
            else:
                res = min(res, nums[mid])
                right = mid - 1
        return res

# # [2, 1]
#    lm  r
