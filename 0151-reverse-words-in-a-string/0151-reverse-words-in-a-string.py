class Solution(object):
    def reverseWords(self, s):
        num = s.split()
        num.reverse()
        result =" ".join(num)

        return result
     
        