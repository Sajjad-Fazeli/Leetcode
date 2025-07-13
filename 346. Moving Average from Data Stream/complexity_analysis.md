## Complexity Analysis

Let **`size`** be the window size provided during initialization.

### Time Complexity: O(1)

- **`MovingAverage(int size)` (Constructor):**
    - Initializes the data structure (e.g., a `deque` or list) and a sum variable. This takes constant time, **O(1)**.

- **`next(int val)`:**
    - Adding the new `val` to the window (e.g., `append` to a `deque`) is an **O(1)** operation.
    - Updating the running sum is **O(1)**.
    - If the window exceeds `size`, removing the oldest element (e.g., `popleft` from a `deque`) is an **O(1)** operation.
    - Updating the running sum by subtracting the removed element is **O(1)**.
    - Calculating the average (sum / count) is **O(1)**.
    - Therefore, each call to `next` performs a constant number of operations, resulting in **O(1)** time complexity per call.

### Space Complexity: O(size)

- The `MovingAverage` object needs to store up to `size` elements in its internal data structure (e.g., a `deque` or list) to maintain the current window.
- The maximum value for `size` is 1000, which is a constant. Thus, the space used is proportional to the window size, making it **O(size)**.
