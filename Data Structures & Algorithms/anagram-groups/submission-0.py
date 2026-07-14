class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            anagram[key].append(words)

        return list(anagram.values())
        