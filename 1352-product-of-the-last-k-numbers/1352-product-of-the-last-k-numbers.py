class ProductOfNumbers:

    def __init__(self):
        self.ans = [1]
    def add(self, num):
        if num > 0:
            self.ans.append(self.ans[-1]*num)
            #print(self.ans)
        else:
            self.ans = [1]
        
    def getProduct(self, k: int) -> int:
        if(k<len(self.ans)):
            return self.ans[len(self.ans)-1]//self.ans[len(self.ans)-1-k]
        else:
            return 0
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)