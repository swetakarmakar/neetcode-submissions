class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        max_odd = 0
        min_even = 100

        for freq in count.values():
            if freq % 2 == 1:
                if freq > max_odd:
                    max_odd = freq
            else:
                if freq < min_even:
                    min_even = freq

        return max_odd - min_even