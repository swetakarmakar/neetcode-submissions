class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count={}
        output = 0 

        for c in chars:
            count[c] = count.get(c, 0)+1


        for w in words:
            temp = count.copy()
            possible = True 

            for c in w:
                if c not in temp or temp[c] == 0:
                    possible = False
                    break 

                temp[c] -= 1

            
            if possible:
                    output += len(w)

        return output 