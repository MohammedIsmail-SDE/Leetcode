class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Step 1: find pivot — first index from right where nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: if pivot found, find the smallest number to its right that's bigger, swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: reverse the suffix after pivot (it was non-increasing, now make it ascending)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1