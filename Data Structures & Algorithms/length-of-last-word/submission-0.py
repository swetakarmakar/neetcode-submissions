class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        leng=0
        i =0 
        while i < len(s):
            if s[i] == ' ':
                while i < len(s)and s[i]== ' ':
                    i += 1
                if i == len(s):
                    return leng 
                leng = 0 
                    
            else:
                leng += 1
                i += 1 
        return leng