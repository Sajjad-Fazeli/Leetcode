class Solution:
  def nextGreaterElement(self, nums1, nums2):
    greater_element_map = {}
    stack =  []

    for n in nums2:
      while deq an stack[-1] < n:
            pop_element =stack.pop()
            greater_element_map[pop_element] = n
      stack.append(n)

    results = [greater_element_map.get(n,-1) for n in nums1]
    return results
    
