

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the start and end of the list
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_value = numbers[left] + numbers[right]
            
            if current_value == target:
                # Returns 1-indexed positions as required by the prompt
                return [left + 1, right + 1] 
            elif current_value < target:
                left += 1  # Target is larger, move left pointer right to increase sum
            else:
                right -= 1 # Target is smaller, move right pointer left to decrease sum
      