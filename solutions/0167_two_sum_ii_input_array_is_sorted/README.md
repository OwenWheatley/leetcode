### Step by Step Breakdown:
1. Initialize two pointers: `leftP` at the beginning of the array (`0`) and `rightP` at the end of the array (`len(numbers) - 1`).
2. Use a while loop to iterate as long as `leftP` is less than `rightP`:
   - Calculate the sum of the elements at `leftP` and `rightP` (i.e., `numbers[leftP] + numbers[rightP]`).
   - If the sum equals the target, return the indices `[leftP + 1, rightP + 1]` since the array is 1-indexed.
   - If the sum is less than the target, increment `leftP` to try a larger sum.
   - If the sum is greater than the target, decrement `rightP` to try a smaller sum.
3. The loop guarantees that the correct solution will be found as per the problem constraints (exactly one solution exists).

### Time Complexity:
- **O(n)**, where `n` is the length of the `numbers` array. Each element is visited at most once by either the left or right pointer.

### Space Complexity:
- **O(1)**, since no additional space is used beyond the two pointers and a few variables.

### Code Snippet:
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP, rightP = 0, len(numbers) - 1
        while leftP < rightP:
            current_sum = numbers[leftP] + numbers[rightP]

            if current_sum == target:
                return [leftP + 1, rightP + 1]
            elif current_sum < target:
                leftP += 1
            else:
                rightP -= 1
