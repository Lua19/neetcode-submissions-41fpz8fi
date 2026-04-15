class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}

        for x in strs:
            chars = list(x)
            chars.sort()
            chars = ''.join(chars)
            if chars in anagram_hash:
                anagram_hash[chars].append(x)
            else:
                anagram_hash[chars] = [x]
        res = list(anagram_hash.values())
        return res