class Solution(object):
    def maxSubArray(self, nums):
        max_sub = nums[0]
        sum_num = 0
        for n in nums :
            if sum_num <= 0 :
                sum_num = 0
            sum_num +=n
            max_sub = max( max_sub ,  sum_num)
        return max_sub 
       
        