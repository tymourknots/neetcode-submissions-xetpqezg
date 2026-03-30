class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        string = 0
        start, end = 0, 0

        for i, c in enumerate(s):
            string += 1
            end = max(end, lastIndex[c])

            if i >= end:
                res.append(string)
                start = 0
                string = 0
        
        return res