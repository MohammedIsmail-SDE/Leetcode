class Solution(object):
    def removeOuterParentheses(self, s):
        res=""
        level=0

        for ch in s:
            if ch=='(':
                if level>0:
                    res+=ch
                
                level+=1
            else:
                level-=1
                if level>0:
                    res+=ch
        
        return res