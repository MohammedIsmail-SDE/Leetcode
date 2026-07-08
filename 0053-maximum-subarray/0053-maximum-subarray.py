class Solution(object):
    def maxSubArray(self, nums):
        best = nums[0]
        running_best = 0
        for i in nums:
            running_best += i
            if running_best > best:
                best = running_best
            if running_best < 0:
                running_best = 0
        return best
       
        