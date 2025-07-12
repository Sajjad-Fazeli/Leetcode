class Solution:
  def make_string_great(s):
    stack = []
    for char in s:
      if abs(ord(stack[-1]) - ord(char)) == 32:
        stack.pop()
      else:
        stack.append(char)
    return "".join(stack)
