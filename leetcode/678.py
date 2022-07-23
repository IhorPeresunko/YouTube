class Solution:
    def checkValidString(self, s: str) -> bool:
        opened, stars = 0, 0
        
        for char in s:
            if char == '(':
                opened += 1
            elif char == '*':
                stars += 1
                if opened > 0:
                    opened -= 1
                    stars += 1
            else:
                if opened > 0:
                    opened -= 1
                elif stars > 0:
                    stars -= 1
                else:
                    return False
        
        return opened == 0