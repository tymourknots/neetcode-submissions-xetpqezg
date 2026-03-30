class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def backtrack(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            return (
                backtrack(i + 1, curSum + nums[i]) +
                backtrack(i + 1, curSum - nums[i])
            )
        
        return backtrack(0, 0)