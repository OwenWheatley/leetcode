### Step by Step Breakdown:
1. Initialize an empty list `s2` to store the alphanumeric characters from the string `s` in lowercase.
2. Iterate through each character `c` in the string `s`:
   - If the character is alphanumeric (checked using `isalnum()`), convert it to lowercase and append it to the list `s2`.
3. Initialize two pointers: `leftP` at the start (0) and `rightP` at the end (`len(s2) - 1`) of the list `s2`.
4. Use a while loop to compare the characters at `leftP` and `rightP`:
   - If they are not equal, return `False` as the string is not a palindrome.
   - If they are equal, increment `leftP` and decrement `rightP` to move towards the middle.
5. If all characters match, return `True`, indicating the string is a palindrome.

### Time Complexity:
- **O(n)**, where `n` is the length of the input string `s`. We iterate through the string once to clean it, and then once again to compare characters.

### Space Complexity:
- **O(n)**, since we store the cleaned version of the string in a list `s2`.

### Code Snippet:
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        for c in s:
            if c.isalnum():
                s2.append(c.lower())
        leftP = 0
        rightP = len(s2) - 1
        while leftP < rightP:
            if s2[leftP] != s2[rightP]:
                return False
            leftP += 1
            rightP -= 1
        return True
