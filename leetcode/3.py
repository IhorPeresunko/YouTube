class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory, left, res = set(), 0, 0

        for right, cur_char in enumerate(s):
            while cur_char in memory:
                left_char = s[left]
                memory.remove(left_char)

                left += 1

            memory.add(cur_char)
            res = max(right - left + 1, res)
        
        return res
                