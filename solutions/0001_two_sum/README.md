### [1. Two Sum](https://leetcode.com/problems/two-sum/)
### Step-by-Step Breakdown of the Code

1.  **Initialization**:

    -   A dictionary `thisdict` is initialized as an empty dictionary `{}`. This dictionary will store the numbers seen so far as keys and their corresponding indices as values.
2.  **Iteration over the List**:

    -   The `for` loop iterates through the `nums` list using `enumerate`, which gives both the index `i` and the value `n` of each element.
3.  **Check for Complement**:

    -   For each element `n`, the code checks if `target - n` exists as a key in `thisdict`.
    -   `target - n` represents the value that, when added to `n`, would equal the `target`.
4.  **If Complement Exists**:

    -   If `target - n` exists in `thisdict`, it means we've already seen a number that, when added to `n`, gives the `target`.
    -   In that case, `thisdict.get(target - n)` retrieves the index of the previously seen number, and `i` is the current index. These indices form a pair that satisfies the condition, so the code returns `[thisdict.get(target - n), i]`.
5.  **If Complement Does Not Exist**:

    -   If `target - n` is not in `thisdict`, it means we haven't seen the required complement yet.
    -   The code then updates `thisdict` by adding the current number `n` as a key with its index `i` as the value. This allows future iterations to potentially find a pair with this number.
6.  **Return Value**:

    -   The function returns the indices of the two numbers as a list when the target sum is found. Given the problem's constraints, it's assumed there is always exactly one solution, so the function doesn't need to handle the case where no pair is found.
### Time Complexity

-   **Time Complexity**: O(n)
    -   The code uses a single pass through the `nums` list, where `n` is the length of the list.
    -   Dictionary lookups (checking if an element is in `thisdict` and updating it) take O(1) time on average.
    -   Therefore, the overall time complexity is O(n).

### Space Complexity

-   **Space Complexity**: O(n)
    -   The space complexity is mainly due to storing elements in `thisdict`.
    -   In the worst case, we store every number in the list (if we do not find the pair until the end).
    -   Hence, the space complexity is O(n).

# Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}
        for i, n in enumerate(nums):
            if (target - n) in thisdict:
                return [thisdict.get(target - n), i]
            else:
                thisdict.update({n : i})
```