## Complexity Analysis

Let **N** be the number of days (length of the `temperatures` array).

### Time Complexity: O(N)

- The most common and efficient solution for this problem involves using a monotonic stack.
- Each temperature value from the input array is pushed onto the stack at most once.
- Each temperature value is popped from the stack at most once.
- The main loop iterates through the `temperatures` array exactly `N` times.
- Since each push and pop operation on a stack takes O(1) time, and we perform these operations at most `N` times in total across all iterations, the overall time complexity is linear.

### Space Complexity: O(N)

- We need an `answer` array of size `N` to store the results.
- In the worst-case scenario (e.g., temperatures are in strictly decreasing order like `[100, 90, 80, ...]`), the monotonic stack could potentially store all `N` indices.
- Therefore, the space complexity is proportional to the number of elements in the input array.
