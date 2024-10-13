### 217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

### Step-by-Step Breakdown:

1.  **Initialization**:

    -   Create an empty set called `hashset`. This set will store the elements as we iterate through `nums`.
2.  **Iterate Through `nums`**:

    -   Loop through each element `n` in the list `nums`.
3.  **Check for Duplicates**:

    -   For each element `n`, check if it is already in `hashset`:
        -   **If `n` is found in `hashset`**, it means that `n` has already appeared before, so we return `True` immediately, indicating that there is a duplicate.
        -   **If `n` is not found in `hashset`**, add `n` to `hashset` to track that we've seen this element.
4.  **No Duplicates Found**:

    -   If the loop completes without finding any duplicates, return `False`. This means all elements in `nums` are unique.

### Time Complexity:

-   **Time Complexity**: **O(n)**

    -   The time complexity is `O(n)` where `n` is the length of `nums` because:
        -   We iterate through each element in `nums` exactly once.
        -   Checking for membership in a set and adding an element to a set both have an average time complexity of `O(1)`.
-   **Space Complexity**: **O(n)**

    -   The space complexity is `O(n)` because, in the worst case (when there are no duplicates), we may store all `n` elements of `nums` in `hashset`.

# Code
```python3 []
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
```