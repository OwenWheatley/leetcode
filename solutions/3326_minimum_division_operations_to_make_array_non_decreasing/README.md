### Step by Step Breakdown:
1. **Helper Function (Greatest Proper Divisor)**: 
   - Use a helper function `greatest_proper_divisor(x)` to compute the largest proper divisor of `x`. A proper divisor is a number less than `x` that divides `x`. This function starts checking from `x // 2` downwards and returns the first divisor found, or 1 if none exists.
   - Apply `lru_cache` to cache the results of this function to optimize repeated calculations for the same number.
   
2. **Initial Check**: 
   - If the array `nums` is already non-decreasing (i.e., `nums[i] <= nums[i+1]` for all `i`), return `0` because no operations are required.
   
3. **Main Loop**:
   - Iterate through the array `nums` from right to left (starting at the second last element).
   - For each element `nums[i]`, check if it's greater than the next element (`nums[i] > nums[i+1]`):
     - Repeatedly divide `nums[i]` by its greatest proper divisor (`gpd`) and increment the `ans` counter to keep track of the number of operations.
     - If the greatest proper divisor is `1` and `nums[i]` is still greater than `nums[i+1]`, return `-1`, as it's impossible to make the array non-decreasing.
   - If `nums[i]` becomes 1 and is still greater than `nums[i+1]`, return `-1`.

4. **Return the Result**: 
   - After processing all elements, return the total count of operations (`ans`).

### Time Complexity:
- **O(n * sqrt(m))**, where `n` is the length of `nums` and `m` is the maximum value in `nums`. For each element, calculating the greatest proper divisor could take up to `O(sqrt(m))` time due to the iterative check for divisors.

### Space Complexity:
- **O(n)**, due to the recursive call stack and caching from `lru_cache`.

### Code Snippet:
```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def greatest_proper_divisor(x: int) -> int:
            for i in range(x // 2, 0, -1):
                if x % i == 0:
                    return i
            return 1

        if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
            return 0

        ans = 0

        for i in range(len(nums) - 2, -1, -1):
            while nums[i] > nums[i + 1]:
                gpd = greatest_proper_divisor(nums[i])
                
                if gpd == 1:
                    return -1
                
                nums[i] //= gpd
                ans += 1

                if nums[i] == 1 and nums[i] > nums[i + 1]:
                    return -1

        return ans
