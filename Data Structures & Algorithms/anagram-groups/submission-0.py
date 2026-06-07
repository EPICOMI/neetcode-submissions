class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        # create a map for the anagrams to sorted anagram : value -> key
        anagram_map = defaultdict(list)
        # sort the anagrams and append each anagram in the list of strings
        # to the list that is identified by that sorted_key
        for s in strs:
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
        # we want to return a list of the anagram map's values
        # which will automatically be separated by sorted_key
        return list(anagram_map.values())