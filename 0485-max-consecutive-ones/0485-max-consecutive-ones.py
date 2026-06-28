class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l = 0
        r = 0
        for num in nums :
            if num == 1 :
                l+=1
            else:
                l = 0 

            if l > r :
                r = l 
        return r
        
      


       
        