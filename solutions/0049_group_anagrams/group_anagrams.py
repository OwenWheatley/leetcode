class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            sdict[key].append(s)
        return list(sdict.values())