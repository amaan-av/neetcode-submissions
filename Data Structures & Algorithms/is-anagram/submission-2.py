class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countt=len(t)
        counts=len(s)
        if counts!=countt:
            return False
        
        c={}

        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for i in t:
            if i not in c:
                return False
            c[i]-=1
            if c[i]<0:
                return False
        return True

            