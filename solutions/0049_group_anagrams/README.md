### Step by Step Breakdown:
1. Initialize a `defaultdict` called `sdict` where the keys will be sorted versions of the strings and the values will be lists of anagrams corresponding to those keys.
2. Loop through each string `s` in the input list `strs`:
   - For each string, sort the characters and use the sorted string as the key in `sdict`.
   - Append the original string `s` to the list corresponding to the sorted key.
3. After processing all strings, return the values of `sdict`, which are lists of grouped anagrams.

### Time Complexity:
- **O(n * k log k)**, where `n` is the number of strings and `k` is the maximum length of a string. Sorting each string takes O(k log k), and this is done for all `n` strings.

### Space Complexity:
- **O(n * k)**, where `n` is the number of strings and `k` is the maximum length of a string. The extra space is used to store the grouped anagrams in the dictionary.

### Code Snippet:
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            sdict[key].append(s)
        return list(sdict.values())
