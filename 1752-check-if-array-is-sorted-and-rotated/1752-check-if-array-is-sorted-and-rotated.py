class Solution(object):
    def check(self, nums):
        n=len(nums)
        if n<2:
            return True
        k=-1
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                k=i
                break
        if k==-1:
            return True       
        
        for i in range(n-1):
            x=(k+i)%n
            if nums[x%n]>nums[(x+1)%n]:
                return False
        return True
        