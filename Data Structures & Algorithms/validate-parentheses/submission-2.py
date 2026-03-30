class Solution:
    def isValid(self, s: str) -> bool:
        match = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or stack.pop() != match[char]:
                    return False
            else:
                return False
        return len(stack) == 0