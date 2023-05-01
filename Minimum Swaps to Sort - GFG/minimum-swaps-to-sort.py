from collections import OrderedDict

class Solution:
    def minSwaps(self, nums):
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



            



#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends