class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            dp[(i, curSum)] = (
                backtrack(i + 1, curSum + nums[i]) + 
                backtrack(i + 1, curSum - nums[i])
            )

            return dp[(i, curSum)]

        return backtrack(0, 0)