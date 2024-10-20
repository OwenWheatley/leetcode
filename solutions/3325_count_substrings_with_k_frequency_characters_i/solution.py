class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        leftP = 0
        ans = 0

        for rightP in range(len(s)):
            freq[s[rightP]] += 1

            while any(freq[char] >= k for char in freq):
                ans += len(s) - rightP
                freq[s[leftP]] -= 1
                if freq[s[leftP]] == 0:
                    del freq[s[leftP]]
                leftP += 1
        return ans