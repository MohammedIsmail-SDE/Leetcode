class Solution(object):
    def reverse(self, x):
        # 1. Determine if the number is negative
        sign = -1 if x < 0 else 1
        
        # 2. Reverse the absolute value using string slicing [::-1]
        reversed_str = str(abs(x))[::-1]
        reversed_int = sign * int(reversed_str)
        
        # 3. Check for 32-bit signed integer overflow bounds
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int
