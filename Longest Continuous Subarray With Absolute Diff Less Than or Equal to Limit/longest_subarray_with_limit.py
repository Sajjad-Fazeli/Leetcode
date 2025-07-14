from collection import deque
class Solution:
  def longestSubarray(self, nums, limit):
    decreasing = deque()
    increasing = deque()
    max_length = 0
    left = 0

    for right in range(len(nums)):

      while decreasing and nums[decreasing[-1]] <= nums[right]:
          decreasing.pop()
      decreasing.append(right)

      while increasing and nums[increasing[-1]] >= nums[right]:
          increasing.pop()
      increasing.append(right)

      while nums[decreasing[0]] - nums[increasing[0]] > limit:
        left += 1
        if max_deque[0] < left:
                max_deque.popleft()
        if min_deque[0] < left:
                min_deque.popleft()
      max_len = max(max_len, right - left + 1)
  return max_len
    
        
