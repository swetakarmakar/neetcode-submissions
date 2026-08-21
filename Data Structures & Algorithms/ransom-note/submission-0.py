class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        countRN = Counter(ransomNote)
        countM = Counter (magazine)

        
        for char in countRN:
            if countM[char] < countRN[char]:
                    return False
        
        
        return True 