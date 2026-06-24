class Solution(object):
    def check(self, nums):
        if len(nums) == 1:
            return True

        # check if already sorted or not
        def _check_sorted(n):
            for i in range(1, len(n)):
                if n[i -1] > n[i]:
                    return False
            return True
         
        if _check_sorted(nums):
            return True

        for i in range(len(nums)):
           el =  nums.pop(0)
           nums.append(el)
           if _check_sorted(nums):
            return True
        
        return False


        

'''


'''   
       
        