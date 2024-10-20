### Step by Step Breakdown:
1. First, check if the lengths of `s` and `t` are the same. If not, return `False` immediately because strings of different lengths cannot be anagrams.
2. Initialize two dictionaries, `countS` and `countT`, to keep track of the frequency of each character in strings `s` and `t`, respectively.
3. Loop through each character in `s` and `t` simultaneously:
   - For each character in `s`, update its count in `countS`.
   - For each character in `t`, update its count in `countT`.
4. After the loop, compare the character frequencies in `countS` and `countT`:
   - If for any character in `countS`, its frequency doesn't match the corresponding frequency in `countT`, return `False`.
5. If all character frequencies match, return `True`, indicating that `t` is an anagram of `s`.

### Time Complexity:
- **O(n)**, where `n` is the length of `s` (or `t`, since their lengths must be the same). We loop through both strings once to build the frequency dictionaries and once more to compare them.

### Space Complexity:
- **O(1)**, since the dictionaries `countS` and `countT` only store up to 26 characters (lowercase English letters), which is constant space regardless of input size.

### Code Snippet:
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
                
        return True
