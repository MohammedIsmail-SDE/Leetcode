class Solution(object):
    def check(self, nums):
        n=len(nums)
        count=0
        for i in range(0,n):
            if nums[i]>nums[(i+1)%n]:
                count = count+1
        return count<=1
    
        
        return False
        