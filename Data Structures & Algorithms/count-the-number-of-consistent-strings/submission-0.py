class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0 
        for word in words:
            consistent = True 


            for char in word:
                if char not in allowed:
                    consistent = False

                    break 

            if consistent == True :
                consistent_count += 1 

        return consistent_count 
