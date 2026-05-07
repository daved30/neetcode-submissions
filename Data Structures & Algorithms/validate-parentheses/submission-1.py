class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {')': '(', '}': '{', ']': '['}
        for c in s:
            if not c in closed:
                stack.append(c)
            elif c in closed:
                if not stack or stack[-1] != closed[c]:
                    return False
                stack.pop()
        return not stack