class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        start, end = 0, 0
        string = 0
        for i, c in enumerate(s):
            string += 1
            end = max(end, lastIndex[c])

            if i >= end:
                res.append(string)
                string = 0
                start = i + 1
        return res