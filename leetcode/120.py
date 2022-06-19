# 120. Triangle
# https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = [[sys.maxsize] * n for i in range(2)]
        memo[0][0] = triangle[0][0]
        
        for i in range(1, n):
            for j, num in enumerate(triangle[i]):
                memo[i % 2][j] = min(memo[(i - 1) % 2][j], memo[(i - 1) % 2][max(j - 1, 0)]) + triangle[i][j]
                
        return min(memo[(n - 1) % 2])