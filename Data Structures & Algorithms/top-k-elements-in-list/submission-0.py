class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        count = {} # key: the actual number, val: the count of that number
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            buckets[cnt].append(num)
        
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res