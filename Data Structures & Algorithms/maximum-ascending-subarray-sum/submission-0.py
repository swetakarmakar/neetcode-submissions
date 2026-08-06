class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = 0
        maximum = 0 

        for i in range(len(nums)):

            if nums[i] > nums[i - 1]:
                current += nums[i]

            else:
                current = nums[i] 


            maximum = max(maximum , current) 

        return maximum