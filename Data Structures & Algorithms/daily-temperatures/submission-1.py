class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                index = stack.pop()
                res[index[1]] += (i - index[1])
                
            stack.append([t, i])
        return res