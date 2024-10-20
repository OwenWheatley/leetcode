### Step by Step Breakdown:
1. Initialize two pointers: `l` (left) set to 0 (the day we might buy the stock), and `r` (right) set to 1 (the day we might sell the stock).
2. Initialize `maxP` to 0 to keep track of the maximum profit found so far.
3. Use a while loop to iterate through the prices list with `r` as the moving pointer:
   - If the price at `l` is less than the price at `r`, calculate the profit (`prices[r] - prices[l]`) and update `maxP` if this profit is greater than the current `maxP`.
   - If the price at `l` is greater than or equal to `r`, update `l` to be equal to `r`, since buying on a higher-priced day is not optimal.
4. Continue iterating through the list until the end. Once all possible transactions have been checked, return `maxP` as the maximum profit. If no profit is found, `maxP` remains 0.

### Time Complexity:
- **O(n)**, where `n` is the length of the `prices` array. We only iterate through the list once with two pointers.

### Space Complexity:
- **O(1)**, since we only use a few extra variables for tracking the pointers and maximum profit.

### Code Snippet:
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
