class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        j = 0
        for i in pushed:
            stk.append(i)
            while stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        return not stk

                    