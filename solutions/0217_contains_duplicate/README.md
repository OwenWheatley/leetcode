### Step by Step Breakdown:
1. Initialize an empty set `hashset` to keep track of unique numbers we've encountered in the array.
2. Iterate through each element `n` in the `nums` array:
   - If `n` is already present in `hashset`, return `True` as it means the number has appeared at least twice.
   - If `n` is not in `hashset`, add it to the set and continue checking the remaining numbers.
3. If the loop completes without finding any duplicates, return `False`, indicating all elements are distinct.

### Time Complexity:
- **O(n)**, where `n` is the length of the input array `nums`. Each lookup and insertion in a set takes O(1) on average, so we only need to traverse the list once.

### Space Complexity:
- **O(n)**, since we store up to `n` unique elements in the `hashset`.

### Code Snippet:
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
