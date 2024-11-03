### Step by Step Breakdown:
1. **Build the Tree Structure**:
   - Initialize a dictionary `tree` to represent the tree, where each node maps to a list of its children.
   - Populate `tree` using the `parent` array, where each node `child` is added to the list of its parent `par`.

2. **Adjust Parents Based on Matching Characters**:
   - Initialize `myMap`, a dictionary to keep track of the latest occurrence of each character in the path from the root.
   - Define a DFS function `dfs_adjust_parents(node)` that:
     - Checks if there exists an ancestor of the same character as the current node `node`. If found, update the parent of `node` to this ancestor.
     - Append `node` to `myMap[char]` and continue DFS on each child.
     - After processing all children, remove `node` from `myMap[char]` to backtrack properly.

3. **Calculate Subtree Sizes**:
   - Define a DFS function `dfs_calculate_sizes(node)` to compute the size of the subtree rooted at each node:
     - Initialize `size` to `1` (counting the node itself).
     - For each child of `node`, recursively calculate the size and add it to `size`.
     - Store `size` in the `ans` array for the current node and return `size` for parent calculations.

4. **Execute DFS Functions**:
   - First, call `dfs_adjust_parents(0)` to adjust the tree structure based on character matching.
   - Then, call `dfs_calculate_sizes(0)` to compute the sizes of the subtrees in the final tree structure.

5. **Return the Result**:
   - Return `ans`, the array containing the subtree sizes for each node.

### Time Complexity:
- **O(n)**, where `n` is the number of nodes. Each node is visited once during the parent adjustment and once during subtree size calculation.

### Space Complexity:
- **O(n)**, due to the storage used for the `tree`, `myMap`, and `ans` arrays.

### Code Snippet:
```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = defaultdict(list)
        
        for child, par in enumerate(parent):
            if par != -1:
                tree[par].append(child)
        
        myMap = defaultdict(list)
        ans = [0] * n
        
        def dfs_adjust_parents(node: int) -> None:
            char = s[node]
            if myMap[char]:
                closest_ancestor = myMap[char][-1]
                if parent[node] != closest_ancestor:
                    tree[parent[node]].remove(node)
                    tree[closest_ancestor].append(node)
                    parent[node] = closest_ancestor
            
            myMap[char].append(node)
            
            for child in list(tree[node]):
                dfs_adjust_parents(child)
            
            myMap[char].pop()
        
        def dfs_calculate_sizes(node: int) -> int:
            size = 1
            for child in tree[node]:
                size += dfs_calculate_sizes(child)
            ans[node] = size
            return size
        
        dfs_adjust_parents(0)
        
        dfs_calculate_sizes(0)
        
        return ans
