class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Functional Requirements
        1. Anagram is a word with the same number of characters as another
        2. Output is returned in any order
        3. Group anagrams together into sublists

        Example
        '''

        # hm = defaultdict(list)
        hm = {}
        for val in strs:
            # O(nlogn)
            characters = sorted([c for c in val])
            key = tuple(characters)

            if key not in hm:
                hm[key] = []

            hm[key].append(val)

        return list(hm.values())