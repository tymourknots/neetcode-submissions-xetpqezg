class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


# [1, 2, 0, 1, 0]

# goal = index 4
# i = index 3
# if index 3 + nums[index 3] >= goal: goal = index 3
# goal = 3, i = 2

# if 2 + nums[2] = 2 + 0 >= goal, 2 < 3 so goal = 3
# goal = 3, i = 1
# if 1 + nums[1] = 1 + 2 >= goal, goal = 1
# goal = 1, i = 0
# if 0 + nums[0] = 0 + 1 >= goal 1 = 1, goal = 0
# end loop
# we traversed the whole loop, return True
# if goal > 0, then we werent able to reach the goal index from the start and return False 