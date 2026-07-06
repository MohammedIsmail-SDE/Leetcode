class Solution(object):
    def rearrangeArray(self, nums):
        i = 0 
        j = 1
        Res = [0]*len(nums)
        for k  in range(len(nums)):
            if nums [k] > 0 :
                Res[i] = nums[k]
                i += 2
            else :
                Res[j] = nums[k]
                j += 2
        return Res

        
        