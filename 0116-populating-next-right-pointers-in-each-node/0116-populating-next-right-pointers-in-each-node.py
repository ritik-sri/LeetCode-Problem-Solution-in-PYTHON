class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        q = []
        q.append(root)
        q.append(None)
        while len(q) > 1:
            for i in range(len(q)):
                ele = q.pop(0)
                ele.next = q[0]
                if ele.left != None:
                    q.append(ele.left)
                if ele.right != None:
                    q.append(ele.right)
                if ele.next == None:
                    q.pop(0)
                    break
            q.append(None)
        return root