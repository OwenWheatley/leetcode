### Step by Step Breakdown:
1. Initialize three dictionaries (`cols`, `rows`, and `squares`) using `collections.defaultdict(set)`. These will store the seen values for each column, row, and 3x3 sub-box, respectively.
2. Iterate over every cell in the 9x9 `board` using two nested loops to check each row `r` and column `c`:
   - Skip cells that contain a period ('.') as they are empty and don't need to be validated.
   - For non-empty cells, check if the current value already exists in the corresponding row, column, or sub-box:
     - If the value exists in any of these, return `False` since it violates the Sudoku rules.
     - Otherwise, add the value to the corresponding row, column, and sub-box sets.
3. If no rule violations are found after checking all cells, return `True`, indicating the board is valid.

### Time Complexity:
- **O(1)**: Since the size of the board is fixed at 9x9, we perform a constant number of operations regardless of the input size.

### Space Complexity:
- **O(1)**: We use a constant amount of extra space (three dictionaries), which is also independent of the board size.

### Code Snippet:
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
