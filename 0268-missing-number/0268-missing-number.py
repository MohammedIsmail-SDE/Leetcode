class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        num = n *(n+1)//2
        missing = num - sum(nums)

        return missing
       
        