### Step by Step Breakdown:
1. Convert the integer `x` to a string `strX` so that we can easily check whether it reads the same from both directions (left to right and right to left).
2. Initialize two pointers: `leftP` at the beginning of the string (`0`) and `rightP` at the end of the string (`len(strX) - 1`).
3. Use a while loop to compare the characters at `leftP` and `rightP`:
   - If the characters at `leftP` and `rightP` are not equal, return `False` as the number is not a palindrome.
   - If the characters match, increment `leftP` and decrement `rightP` to move towards the middle.
4. If the loop completes without returning `False`, return `True`, indicating the integer is a palindrome.

### Time Complexity:
- **O(n)**, where `n` is the number of digits in `x`. We compare digits from both ends, which takes linear time.

### Space Complexity:
- **O(n)**, due to the conversion of the integer to a string, which takes up space proportional to the number of digits in `x`.

### Code Snippet:
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        leftP, rightP = 0, len(strX) - 1
        while leftP < rightP:
            if strX[leftP] != strX[rightP]:
                return False
            leftP += 1
            rightP -= 1
        return True
