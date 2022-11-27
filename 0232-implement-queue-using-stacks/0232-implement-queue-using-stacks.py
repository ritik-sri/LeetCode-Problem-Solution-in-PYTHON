class MyQueue:
    def __init__(self):
        self.kuchbhi=[]
        

    def push(self, x: int) -> None:
        self.kuchbhi.append(x)
        

    def pop(self) -> int:
        return self.kuchbhi.pop(0)
        

    def peek(self) -> int:
        return self.kuchbhi[0]
        

    def empty(self) -> bool:
        if not self.kuchbhi:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()