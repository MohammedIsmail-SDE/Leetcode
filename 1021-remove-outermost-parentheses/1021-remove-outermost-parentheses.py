class Solution(object):
    def removeOuterParentheses(self, s):
        res=""
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                if count>1:
                    res+=s[i]
            else:
                count-=1
                if count>0:
                    res+=s[i]
        return res

        
            
        