class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
    
            while left < right:
                total = a + nums[left] + nums[right]
                if total == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return res