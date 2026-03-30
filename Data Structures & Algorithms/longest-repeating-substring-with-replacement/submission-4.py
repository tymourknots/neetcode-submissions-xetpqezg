class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1 
            length = right - left + 1
            maxCount = max(count.values())

            if length - maxCount > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


