class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0

        for i in range(len(s)- 1):
            first = ord(s[i])
            second = ord(s[i+1])

            diff = abs(first - second)

            result += diff

        return result