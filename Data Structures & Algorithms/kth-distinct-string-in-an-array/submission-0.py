class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for word in arr:
            if word in count:
                count[word] +=1
            else:
                count[word] = 1

        distinct = 0

        for word in arr:
            if count[word] == 1:
                distinct +=1

                if distinct == k:
                    return word

        return ""