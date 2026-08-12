class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:                      # закрывающая
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:                                # открывающая
                stack.append(ch)

        return not stack



