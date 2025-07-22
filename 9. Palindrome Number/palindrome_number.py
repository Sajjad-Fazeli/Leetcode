class Solution:
  def isPalindrom(x):
    x = str(x)
    return x == x[::-1]

  def isPalindrom_optimal(x):
    if x < 0 or ( x == 0 or x % 10 == 0):
       return False
    half = 0
    while half < x:
      half = (half*10) + (x % 10)
      x = x // 10
    return x == half or x == half // 10
    
