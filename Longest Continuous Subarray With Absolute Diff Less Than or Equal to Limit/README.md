
# Longest Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers `nums` and an integer `limit`, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

---

## Examples

### Example 1:
```
Input: nums =, limit = 4
Output: 2 

Explanation: 
Let's examine all subarrays and their maximum absolute differences:
- : |8-8| = 0 <= 4
- : |8-2| = 6 > 4
- : |8-2| = 6 > 4
- : |8-2| = 6 > 4
- : |2-2| = 0 <= 4
- : |2-4| = 2 <= 4
- : |2-7| = 5 > 4
- : |4-4| = 0 <= 4
- : |4-7| = 3 <= 4
- : |7-7| = 0 <= 4

The longest valid subarrays are and, both with size 2.
```

### Example 2:
```
Input: nums =, limit = 5
Output: 4 

Explanation: 
The subarray (from index 2 to 5) has a maximum absolute difference of |2-7| = 5, which is <= 5. No longer subarray satisfies the condition.
```

### Example 3:
```
Input: nums =, limit = 0
Output: 3

Explanation:
With limit = 0, all elements in a valid subarray must be identical. 
The longest such subarray is or. Both have size 3.


## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`
```
