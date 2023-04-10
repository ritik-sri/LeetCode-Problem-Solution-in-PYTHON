class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                l.append(i)
            elif i==')':
                if len(l)!=0:
                    if l[-1]=='(':
                        l.pop()
                    else:
                        return False
                else:
                    return False
            elif i=='}':
                if len(l)!=0:
                    if l[-1]=='{':
                        l.pop()
                    else:
                        return False
                else:
                    return False
            elif i==']':
                if len(l)!=0:
                    if l[-1]=='[':
                        l.pop()
                    else:
                        return False
                else:
                    return False
        #print(l)
        return len(l)==0