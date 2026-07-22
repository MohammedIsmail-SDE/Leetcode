class Solution(object):
    def isPalindrome(self, x):
        
        rev=str(x)[::-1]
        if rev==str(x):
            return True
        else:
            return False



        