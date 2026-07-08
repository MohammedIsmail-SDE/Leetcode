class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        longest=0
        for i in s:
            if i-1 not in s:
                curr=1
                while i+curr in s:
                    curr=curr+1
                longest=max(longest,curr)
                if longest>len(nums)/2:
                    return longest
        return longest
            

      