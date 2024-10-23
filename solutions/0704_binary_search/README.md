### Step by Step Breakdown:
1. **Initialize Pointers**: Set two pointers: `leftP` at the start of the array (`0`) and `rightP` at the end of the array (`len(nums) - 1`).
2. **Binary Search Loop**: Use a while loop that continues as long as `leftP` is less than or equal to `rightP`:
   - Calculate the middle index `m` using `m = leftP + ((rightP - leftP) // 2)` to prevent overflow in large arrays.
   - If `nums[m]` is greater than the target, move the `rightP` pointer to `m - 1`, as the target must be in the left half of the array.
   - If `nums[m]` is less than the target, move the `leftP` pointer to `m + 1`, as the target must be in the right half of the array.
   - If `nums[m]` equals the target, return `m` as the index of the target.
3. **Return Result**: If the loop exits without finding the target, return `-1`, indicating the target is not present in the array.

### Time Complexity:
- **O(log n)**, where `n` is the length of the input array `nums`. This is due to the binary search approach, which repeatedly halves the search space.

### Space Complexity:
- **O(1)**, as the algorithm only uses a few variables for the pointers and the middle index, without requiring additional space.

### Code Snippet:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftP, rightP = 0, len(nums) - 1

        while leftP <= rightP:
            m = leftP + ((rightP - leftP) // 2)
            if nums[m] > target:
                rightP = m - 1
            elif nums[m] < target:
                leftP = m + 1
            else:
                return m
        return -1
