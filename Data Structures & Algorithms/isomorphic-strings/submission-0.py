class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map={}
        t_map = {}

        for i in range(len(s)):
            a= s[i]
            b= t[i]

            if a in s_map and s_map[a] != b:
                return False 
            if b in t_map and t_map[b] != a:
                return False

            s_map[a] = b
            t_map[b]= a 

        return True