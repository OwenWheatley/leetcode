### Step by Step Breakdown:
1. Initialize an empty list `ans` to store all the strings that appear on the screen.
2. Initialize `current_string` as an empty string, which will track what is currently on the screen.
3. Create a dictionary `next_letter` to map each letter to its next letter in the alphabet. For example, `'a'` maps to `'b'`, `'b'` maps to `'c'`, and so on. The letter `'z'` maps to `'a'` (cyclically).
4. Iterate through each character `c` in the `target` string:
   - First, append the character `'a'` to `current_string` and add this string to `ans`.
   - Then, repeatedly press key 2 to change the last character of `current_string` until it matches `c`. After each change, append the updated string to `ans`.
5. Once all characters of `target` are typed, return the list `ans` containing all strings that appeared on the screen.

### Time Complexity:
- **O(n)**, where `n` is the length of the target string. For each character in `target`, the process of typing (pressing key 1 and potentially key 2) runs in constant time.

### Space Complexity:
- **O(n)**, since we store the strings in the result list `ans`, which grows in proportion to the length of `target`.

### Code Snippet:
```python
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        current_string = ""

        next_letter = {chr(i): chr((i - ord('a') + 1) % 26 + ord('a')) for i in range(ord('a'), ord('z') + 1)}

        for c in target:
            current_string += 'a'
            ans.append(current_string)

            while current_string[-1] != c:
                current_string = current_string[:-1] + next_letter[current_string[-1]]
                ans.append(current_string)

        return ans
