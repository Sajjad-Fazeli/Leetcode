class StockSpanner:

    def __init__(self):
        self.stack = []
    
    def next(self, price):
        current_span = 1
        while self.stack and self.stack[-1][0] <= price:
              previous_span = self.stack.pop()[1]
              current_span += previous_span

        self.stack.append((price, current_span))

        return current_span
