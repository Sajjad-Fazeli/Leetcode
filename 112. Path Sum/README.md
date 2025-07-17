
# Path Sum

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

---

## Examples

### Example 1:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Explanation:
The path 5 -> 4 -> 11 -> 2 has a sum of 5 + 4 + 11 + 2 = 22.
```
*Visual representation of the tree with the path highlighted would typically be included here if this were an image.*

### Example 2:
```
Input: root =, targetSum = 5
Output: false

Explanation:
There are two root-to-leaf paths:
- 1 -> 2 (Sum: 1 + 2 = 3)
- 1 -> 3 (Sum: 1 + 3 = 4)
Neither path sums to 5.
```

### Example 3:
```
Input: root = [], targetSum = 0
Output: false

Explanation:
Since the tree is empty, there are no root-to-leaf paths to check.

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`
```
