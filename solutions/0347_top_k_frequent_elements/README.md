### Step by Step Breakdown:
1. Initialize an empty dictionary `seen_count_dict` to store the frequency of each element in the input array `nums`.
2. Loop through each element `n` in `nums`:
   - For each element, update its frequency in `seen_count_dict` using `get()` to increment the count.
3. After building the frequency dictionary, use Python's `sorted()` function to sort the keys of `seen_count_dict` by their frequency values in descending order (`reverse=True`).
4. Return the first `k` elements of the sorted keys list, which corresponds to the `k` most frequent elements in `nums`.

### Time Complexity:
- **O(n log n)**, where `n` is the length of the `nums` array. The sorting operation dominates the time complexity, and we perform one pass over the input to count frequencies.

### Space Complexity:
- **O(n)**, where `n` is the number of elements in `nums`. We use a dictionary to store the frequency of each element.

### Code Snippet:
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count_dict = {}

        for n in nums:
            seen_count_dict[n] = seen_count_dict.get(n, 0) + 1
            
        return sorted(seen_count_dict, key=seen_count_dict.get, reverse=True)[:k]
