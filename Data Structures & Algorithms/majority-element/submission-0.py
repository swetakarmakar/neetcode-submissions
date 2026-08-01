class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            count = 0

            for value in nums:
                if value == num:
                    count += 1


                if count > len(nums)//2:
                    return num