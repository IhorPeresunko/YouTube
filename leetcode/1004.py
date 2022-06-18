# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        res = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                while zeros >= k:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1
                zeros += 1
            
            res = max(right - left + 1, res)
        
        return res