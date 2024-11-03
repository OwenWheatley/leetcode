### Step by Step Breakdown:
1. **Initialize Variables**:
   - Set `possible_count` to `1`, which will count the total possible original strings.
   - Use a variable `i` to iterate through the string `word`.

2. **Traverse the String**:
   - Use a nested loop to find consecutive characters in `word`:
     - Set `j` to the same position as `i` and increment `j` while characters `word[j]` are the same as `word[i]`.
     - After the loop, `j - i` gives the count of consecutive identical characters starting from index `i`.
   - If the `consecutive_count` (or `j - i`) is greater than 1, it indicates Alice might have held this key too long, so increment `possible_count` by `consecutive_count - 1`.
   - Move `i` to `j` to continue checking the next set of characters.

3. **Return the Result**:
   - After iterating through the string, return `possible_count`, which contains the total number of possible original strings Alice may have intended to type.

### Time Complexity:
- **O(n)**, where `n` is the length of `word`. We traverse each character once to count consecutive characters.

### Space Complexity:
- **O(1)**, as we only use a fixed amount of extra space for counters and indices.

### Code Snippet:
```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        if not word:
            return 0
        
        possible_count = 1
        i = 0
        
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            consecutive_count = j - i
            
            if consecutive_count > 1:
                possible_count += consecutive_count - 1
            
            i = j
            
        return possible_count
