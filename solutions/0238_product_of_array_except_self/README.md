### Step by Step Breakdown:
1. Initialize a result array `res` with the same length as `nums`, and set all elements to 1. This array will hold the final products.
2. Initialize `prefix` to 1, which will store the product of all elements before the current index as we iterate from left to right.
   - Loop through `nums`, and for each element `i`, set `res[i]` to the value of `prefix`, then update `prefix` by multiplying it with `nums[i]`.
3. Initialize `postfix` to 1, which will store the product of all elements after the current index as we iterate from right to left.
   - Loop through `nums` backwards, and for each element `i`, multiply `res[i]` by `postfix`, then update `postfix` by multiplying it with `nums[i]`.
4. Return the result array `res`, which now contains the product of all elements except the one at each index.

### Time Complexity:
- **O(n)**, where `n` is the length of the input array `nums`. We make two passes through the array: one to calculate the prefix products and one for the postfix products.

### Space Complexity:
- **O(1)** extra space, as we are using the `res` array to store the results directly and only a couple of extra variables (`prefix` and `postfix`). The output array `res` is not considered extra space as per the problem constraints.

### Code Snippet:
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
