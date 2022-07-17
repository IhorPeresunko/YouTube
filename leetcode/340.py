class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        memory, left, res = collections.defaultdict(int), 0, 0

        for right, cur_char in enumerate(s):            
            memory[cur_char] += 1

            while len(memory) > k:
                left_char = s[left]
                memory[left_char] -= 1
                
                if memory[left_char] == 0:
                    del memory[left_char]

                left += 1
            
            res = max(right - left + 1, res)
        
        return res