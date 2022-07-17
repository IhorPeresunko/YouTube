class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memory, left, res = collections.defaultdict(int), 0, [0, sys.maxsize]
        cur_size = 0
        
        for char in t:
            memory[char] += 1

        for right, cur_char in enumerate(s):
            if cur_char in memory:
                memory[cur_char] -= 1

                if memory[cur_char] == 0:
                    cur_size += 1
            
            while cur_size == len(memory):
                cur_len = right - left
                prev_len = res[1] - res[0]

                if cur_len < prev_len:
                    res[0] = left
                    res[1] = right
                
                left_char = s[left]
                if left_char in memory:
                    if memory[left_char] == 0:
                        cur_size -= 1
                    memory[left_char] += 1
                left += 1
        
        if res[1] == sys.maxsize:
            return ""
        
        return s[res[0]:res[1] + 1]