class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = set(['{', '[', '('])
        for c in s:
            if c in p:
                stack.append(c)
            elif stack and stack[-1] == '{' and c == '}':
                stack.pop()
            elif stack and stack[-1] == '[' and c == ']':
                stack.pop()
            elif stack and stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                return False
        return len(stack) == 0