
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            while l <= r:
                pivot, p = nums[r], l
                for i in range(l, r):
                    if nums[i] <= pivot:
                        nums[p], nums[i] = nums[i], nums[p]
                        p += 1
                nums[p], nums[r] = nums[r], nums[p]

                if p > k:
                    r = p - 1
                elif p < k:
                    l = p + 1
                else:
                    return nums[p]

        return quickSelect(0, len(nums) - 1)