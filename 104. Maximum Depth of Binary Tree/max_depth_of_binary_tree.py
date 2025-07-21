class Solution:
    def maxDepth(self, root):
      if not root:
        return 0
      left_depth = self.maxDepth(root.left)
      right_depth = self.maxDepth(root.right)
      return max(left, right) + 1
    def maxDepth_iter(root):
        if not root:
            return 0
        ans = 0
        stack = [(root,1)]
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans
            
      
