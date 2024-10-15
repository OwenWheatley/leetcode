### [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
### Code Breakdown

1.  **Initialize the Dictionary**:

    `seen_count_dict = {}`

    -   A dictionary `seen_count_dict` is created to store each element from `nums` as a key and its frequency as the corresponding value.
2.  **Count the Frequency of Each Element**:

    `for n in nums:
        seen_count_dict[n] = seen_count_dict.get(n, 0) + 1`

    -   Loop through each element `n` in `nums`.
    -   Use `get(n, 0)` to retrieve the current frequency of `n` from `seen_count_dict`. If `n` is not already in the dictionary, `get` returns `0`.
    -   Increment the frequency of `n` by 1 and store it back in `seen_count_dict`.
    -   After this loop, `seen_count_dict` will contain all elements of `nums` as keys and their counts as values.
3.  **Sort the Dictionary Keys Based on Their Frequencies**:

    `return sorted(seen_count_dict, key=seen_count_dict.get, reverse=True)[:k]`

    -   `sorted()` sorts the keys of `seen_count_dict` based on their values (frequencies), in descending order (`reverse=True`).
    -   `seen_count_dict.get` is used as the key for sorting, which means that elements with higher counts will appear earlier.
    -   `[:k]` selects the top `k` elements from the sorted list.
    -   Finally, return the top `k` most frequent elements.

### Time Complexity

1.  **Counting Elements**: The `for` loop iterating over `nums` runs in O(n) time, where `n` is the length of `nums`.

2.  **Sorting**: The `sorted()` function sorts the dictionary keys by their values, which has a time complexity of O(m log m), where `m` is the number of unique elements in `nums`.

3.  **Slicing**: Extracting the top `k` elements using `[:k]` is O(k).

    The overall time complexity is **O(n + m log m)**, where:

    -   `n` is the size of the input array.
    -   `m` is the number of unique elements in `nums`.
    -   This solution is not better than **O(n log n)** when the number of unique elements `m` is close to `n`.

### Space Complexity

1.  **Dictionary Storage**: `seen_count_dict` uses O(m) space, where `m` is the number of unique elements in `nums`.

2.  **Sorting Space**: The `sorted()` function may use additional space depending on the sorting algorithm, which is O(m) in the worst case.

3.  **Output List**: The final list of `k` elements is O(k).

    The overall space complexity is **O(m)**, primarily due to storing frequencies in `seen_count_dict`.

### Code
```python3 []
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count_dict = {}

        for n in nums:
            seen_count_dict[n] = seen_count_dict.get(n, 0) + 1
        return sorted(seen_count_dict, key=seen_count_dict.get, reverse=True)[:k]
```