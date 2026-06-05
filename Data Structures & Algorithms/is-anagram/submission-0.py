class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create char counter for s
        # create char counter for t
        # compare, if equal = anagram, if not then not

        freqS = {}
        for c in s:
            freqS[c] = freqS.get(c, 0) + 1
        
        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        return freqS == freqT
