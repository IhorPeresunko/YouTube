# 366. Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        mem = collections.defaultdict(list)
        
        def iterate(root):
            if not root:
                return 0

            left = iterate(root.left)
            right = iterate(root.right)
            mem[max(left, right)].append(root.val)
            return max(left, right) + 1
        
        iterate(root)
        
        res, i = [], 0
        while len(mem[i]) > 0:
            res.append(mem[i])
            i += 1
        return res