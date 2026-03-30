class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] += (i - index)
            stack.append([t, i])
        return res


# Input: temperatures = [30,38,30,36,35,40,28]
# stack = [[40, 5], [28, 6]]
# 38 > 30 -> remove 30, append 38
# temp = 30, index = 0
# res[0] += i - index = 1 - 0 = 1
# 30 < 38 -> append 30, leave 38
# 36 > 30 -> remove 30, append 36
# temp = 30, index = 2
# res[2] += 3 - 2 = 1
# 35 < 36 -> append 35, leave 36
# 40 > 35 -> remove 35, append 40
# temp = 35, index = 4
# res[4] += (5 - 4) = 1
# 40 > 36 -> remove 36, leave 40
# temp = 36, index = 3
# res[3] += (5 - 3) = 2
# 40 > 38 -> remove 38, leave 40
# temp = 38, index = 1
# res[1] += (5 - 1) = 4
# 28 < 40 -> append 28, leave 40


# res: [1,4,1,2,1,0,0]