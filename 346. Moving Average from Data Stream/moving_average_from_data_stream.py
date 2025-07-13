from collection import deque
class MovingAverage:
  def __init__(self, size):
    self.size = size
    self.data = deque()
    self.window_sum = 0
  def next(self, value):
    self.data.append(value)
    self.window_sum += value
    if len(self.data) > self.size:
      self.window_sum -= self.data.popleft()
    return self.window_sum/len(self.data)
    
