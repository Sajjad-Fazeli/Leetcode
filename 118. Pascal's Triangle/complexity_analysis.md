## Complexity Analysis

Let **`numRows`** be the number of rows to generate in Pascal's Triangle.

### Time Complexity: O(numRows^2)

- To generate `numRows` rows, each row `i` (0-indexed) requires computing `i+1` elements.
- Each element is calculated by summing two elements from the previous row, which is a constant time operation.
- The total number of elements generated across all `numRows` is the sum of an arithmetic series: `1 + 2 + 3 + ... + numRows = numRows * (numRows + 1) / 2`.
- Therefore, the total time complexity is proportional to the total number of elements, which is **O(numRows^2)**.

### Space Complexity: O(numRows^2)

- The algorithm stores all `numRows` of the Pascal's Triangle.
- The total number of integers stored is `numRows * (numRows + 1) / 2`.
- This means the space required grows quadratically with `numRows`.
- Therefore, the space complexity is **O(numRows^2)**.
