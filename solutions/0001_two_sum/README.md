### Step by Step Breakdown:
1. Initialize an empty dictionary `thisdict` to store the values of numbers we've encountered and their corresponding indices.
2. Iterate through the `nums` array using both the index `i` and the value `n`:
   - For each number `n`, calculate the difference between the `target` and the current number `n`. This difference represents the value needed to form the target sum with the current number.
   - Check if this difference exists in `thisdict`:
     - If it does, return the indices of the difference (from `thisdict`) and the current index `i` as they sum to the target.
     - If it doesn’t, store the current number `n` and its index `i` in `thisdict`.
3. The loop guarantees that a valid solution will be found as per the problem constraints (only one valid solution exists).

### Time Complexity:
- **O(n)**, where `n` is the length of the array. Each lookup in the dictionary takes O(1), and we iterate through the list exactly once.

### Space Complexity:
- **O(n)**, where `n` is the number of elements in the array. We store at most `n` elements in the dictionary.

### Code Snippet:
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}
        for i, n in enumerate(nums):
            if (target - n) in thisdict:
                return [thisdict.get(target - n), i]
            else:
                thisdict.update({n : i})
