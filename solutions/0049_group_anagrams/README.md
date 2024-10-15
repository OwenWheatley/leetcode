### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
### Step-by-Step Breakdown:

1.  **Create a Dictionary to Group Anagrams**:

    -   `sdict = defaultdict(list)`: Creates a `defaultdict` named `sdict` with lists as default values. This will store the grouped anagrams.
2.  **Iterate Through Each String**:

    -   `for s in strs:`: Iterates over each string `s` in the input list `strs`.
3.  **Create a Key by Sorting the String**:

    -   `key = ''.join(sorted(s))`: Sorts the characters in `s` and joins them back into a string to create a key.
        -   For example:
            -   For `"eat"`, the sorted version is `["a", "e", "t"]`, so the key becomes `"aet"`.
            -   For `"tea"`, the sorted version is also `"aet"`, making it an anagram of `"eat"`.
    -   This key will be the same for all anagrams, making it possible to group them together in the dictionary.
4.  **Store the String in the Dictionary**:

    -   `sdict[key].append(s)`: Appends the original string `s` to the list associated with its sorted key `key`. This groups all strings with the same sorted characters.
5.  **Return the Grouped Anagrams**:

    -   `return list(sdict.values())`: Converts the grouped lists of anagrams from `sdict` into a list of lists and returns them.

### Time Complexity: O(n * m log m)

-   **Sorting each string**: Sorting a string of length `m` takes `O(m log m)`.

-   **Iterating through each string**: There are `n` strings, so we sort each one, resulting in `O(n * m log m)`.

-   **Storing the strings in the dictionary**: Inserting into the `defaultdict` and appending to the list is `O(1)` for each string.

-   **Returning the values**: Converting the values of `sdict` into a list of lists is `O(n)` since there are `n` strings in total.

-   **Overall Time Complexity**: `O(n * m log m)`, where `n` is the number of strings and `m` is the maximum length of a string.

### Space Complexity: O(n * m)

-   **Dictionary Storage**: The `sdict` dictionary stores up to `n` strings, and each string can have a length of up to `m`, so this requires `O(n * m)` space.

-   **Space for Sorted Keys**: Sorting each string creates temporary copies, which also take up `O(m)` space.

-   **Output List**: The final output list of lists requires `O(n)` space since it stores references to all input strings.

-   **Overall Space Complexity**: `O(n * m)` due to the storage in the `sdict` and the output list.

# Code
```python3 []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            sdict[key].append(s)
        return list(sdict.values())
```