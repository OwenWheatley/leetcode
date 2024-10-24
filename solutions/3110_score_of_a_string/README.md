### Step by Step Breakdown:
1. **Initialize a Variable**: Set `ans` to `0`, which will store the cumulative score of the string.
2. **Iterate Over the String**: Start a loop from the second character (index 1) to the last character of the string `s`:
   - For each character at position `i`, calculate the absolute difference between its ASCII value (`ord(s[i])`) and the previous character's ASCII value (`ord(s[i-1])`).
   - Add this difference to `ans`.
3. **Return the Result**: After iterating through the entire string, return the total score `ans`.

### Time Complexity:
- **O(n)**, where `n` is the length of the string `s`. The loop iterates through each pair of adjacent characters once.

### Space Complexity:
- **O(1)**, since we only use a constant amount of space to store the result and a few variables.

### Code Snippet:
```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i-1]) - ord(s[i]))
        return ans
