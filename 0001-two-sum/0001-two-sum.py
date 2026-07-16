class Solution:
    def twoSum(self, nums, target):
        notebook = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in notebook:
                return [notebook[need], i]

            notebook[num] = i

        return i 
 


