class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            res = max(res, len(seen))
        return res