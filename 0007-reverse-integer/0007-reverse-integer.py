class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        res=0
        x=abs(x)
        while x>0:
            ld=x%10
            res=(res*10)+ld
            x=x//10
        res*=sign
        if (res<-(2**31) or res>(2**31-1)):
            return 0
        else:
            return res