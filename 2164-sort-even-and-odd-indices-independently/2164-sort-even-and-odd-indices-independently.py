class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        evenArray, oddArray = [], []
        for i in range(len(nums)):
            if i%2==0:
                evenArray.append(nums[i])
            else:
                oddArray.append(nums[i])

        oddArray.sort(reverse=True)
        evenArray.sort()

        for i in range(len(nums)):
            if i%2==0:
                nums[i] = evenArray[0]
                evenArray.pop(0)
            else: 
                nums[i] = oddArray[0]
                oddArray.pop(0)

        return nums