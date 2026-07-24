class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lst= len(arr)
        nums = [0] * lst
        for i in range(lst):
            right= -1
            for j in range(i+1, lst):
                right = max(right, arr[j])
            nums[i]= right
        return nums