## Complexity Analysis of `simplifyPath` Function

Let **N** be the length of the input Unix-style path string.

---

### Time Complexity: O(N)

The overall time complexity is linear relative to the length of the input string due to these main operations:

1. **Splitting the path:**  
   - `components = path.split('/')`  
   - This requires scanning the entire string to identify delimiters, taking **O(N)** time.

2. **Processing components:**  
   - Iterating through each component in `components` involves at most O(N) iterations.  
   - Each iteration performs constant-time operations, such as string comparisons, pushing or popping from the stack.  
   - Total time: **O(N)**.

3. **Joining path components:**  
   - `"/" + "/".join(stack)` concatenates all directory parts into the final string.  
   - This takes **O(N)** time since the total length of the stack elements combined is proportional to `N`.

**Combined:** O(N) + O(N) + O(N) = **O(N)**.

---

### Space Complexity: O(N)

The extra memory used depends mainly on:

1. **`components` list:**  
   - Result of splitting the path on slashes.  
   - The combined length of all strings is at most `N`.  
   - Space: **O(N)**.

2. **`stack` list:**  
   - Stores directory names contributing to the canonical path.  
   - In the worst case, it can contain nearly all components of the original path.  
   - Space: **O(N)**.

**Combined space usage:** O(N) + O(N) = **O(N)**.

---

In summary, the `simplifyPath` function runs in linear time and uses linear auxiliary space relative to the length of the input path.
