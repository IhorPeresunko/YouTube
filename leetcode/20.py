class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        memory = { ')': '(', '}': '{', ']': '[' }
        
        for char in s:
            if char in memory:
                if stack and stack[-1] == memory[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0