from typing import Optional
from collections import deque, OrderedDict

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def minSwaps(nums):
            dic = OrderedDict()
            for i in range(len(nums)):
                dic[nums[i]] = i
            sorted_dic = OrderedDict(sorted(dic.items()))
            swaps = 0
            for i, v in enumerate(sorted_dic.values()):
                if i != v:
                    nums[i], nums[v] = nums[v], nums[i]
                    dic[nums[i]], dic[nums[v]] = dic[nums[v]], dic[nums[i]]
                    sorted_dic[nums[i]], sorted_dic[nums[v]] = sorted_dic[nums[v]], sorted_dic[nums[i]]
                    swaps += 1
            return swaps
        
        if root is None:
            return 0
        
        bfs = []
        q = deque([root])
        level = 0
        count = 0
        
        while q:
            level += 1
            curr_level = []
            for i in range(len(q)):
                curr = q.popleft()
                curr_level.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            
            # Check if current level is already sorted
            if curr_level == sorted(curr_level):
                continue
            else:
                count += minSwaps(curr_level)
            
            bfs.append(curr_level)
        
        return count
