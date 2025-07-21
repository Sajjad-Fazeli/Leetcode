class Solution:
    def maxDepth(self, root):
      if not root:
        return 0
      left_depth = self.maxDepth(root.left)
      right_depth = self.maxDepth(root.right)
      return max(left, right) + 1

      
