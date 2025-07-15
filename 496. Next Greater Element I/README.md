
# Next Greater Element I

The **next greater element** of some element `x` in an array is defined as the first greater element that appears to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays, `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each element in `nums1` (at index `i`), you need to:
1. Find its corresponding element in `nums2`.
2. Determine the next greater element of this corresponding element within `nums2`.
3. If no such next greater element exists to its right in `nums2`, the answer for that query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

---

## Examples

### Example 1:
```
Input: nums1 =, nums2 =
Output: [-1,3,-1]

Explanation:
- For 4 in nums1: Its corresponding value in nums2 is 4 (underlined in). There is no element greater than 4 to its right in nums2. So, the answer is -1.
- For 1 in nums1: Its corresponding value in nums2 is 1 (underlined in). The first element greater than 1 to its right in nums2 is 3. So, the answer is 3.
- For 2 in nums1: Its corresponding value in nums2 is 2 (underlined in). There is no element greater than 2 to its right in nums2. So, the answer is -1.
```

### Example 2:
```
Input: nums1 =, nums2 =
Output: [3,-1]

Explanation:
- For 2 in nums1: Its corresponding value in nums2 is 2 (underlined in). The first element greater than 2 to its right in nums2 is 3. So, the answer is 3.
- For 4 in nums1: Its corresponding value in nums2 is 4 (underlined in). There is no element greater than 4 to its right in nums2. So, the answer is -1.
```

---

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are unique.
- All the integers of `nums1` also appear in `nums2`.
