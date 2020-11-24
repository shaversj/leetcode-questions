class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        if len(s) == 1:
            return False

        for char in s:
            if char in paren:
                stack.append(char)
            else:
                if stack:
                    key = stack.pop()
                    if paren.get(key) == char:
                        continue
                    else:
                        return False
                else:
                    return False

        if len(stack) != 0:
            return False

        return True


s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([)]"))
print(s.isValid("(("))
print(s.isValid(")}"))
print(s.isValid("("))