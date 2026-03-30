class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in '{[(':
                stack.append(c)
            elif c in ')}]':
                if not stack or stack.pop() != valid[c]:
                    return False
            else:
                return False
        return len(stack) == 0
        
