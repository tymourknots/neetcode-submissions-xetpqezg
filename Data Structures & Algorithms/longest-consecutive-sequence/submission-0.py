class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = sorted(set(nums))
        
        total = 0
        for i in range(len(nums)):
            if nums[i] - 1 in seen:
                continue 
            length = 1
            while (nums[i] + length) in seen:
                length += 1
                print(length)
            total = max(total, length)
        return total

    
