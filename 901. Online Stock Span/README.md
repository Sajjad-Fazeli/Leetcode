
# Stock Spanner

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

---

## Span Definition

The **span** of the stock's price on a given day is defined as the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

### Examples for Span Definition:

- If the prices of the stock in the last four days were `[7, 2, 1, 2]` and the price of the stock today is `2`, then the span for today is `4`. This is because, starting from today, the prices `[2, 1, 2, 7]` (reading backward) were all less than or equal to `2` (except for 7, but the span counts consecutive days *less than or equal* to today's price). More accurately, it's `[2, 1, 2]` which are all `<= 2`, and then `7` breaks the condition. The problem statement's example `[7,2,1,2]` implies a span of 4 for today's `2` because `2 <= 2`, `1 <= 2`, `2 <= 2`, and `7` is the first element *greater* than 2. So the span would be 3 (for `[2,1,2]`). Let's clarify based on the general understanding of stock span, which is "consecutive days *before and including* today where price <= today's price". The example `[7,2,1,2]` with today's price `2` having span `4` suggests that the sequence `[2,1,2,7]` (current day and 3 previous days) are all considered, and all are `<= 2` which is incorrect for 7. It usually means `[2,1,2]` and then `7` breaks it, so span is 3. However, the problem statement says "for which the stock price was less than or equal to the price of that day." The example is a bit ambiguous if it means *all* values or just the boundary. Given the standard definition and typical solutions, it usually refers to the count of consecutive days where the price is less than or equal to *today's price*, ending with today. The provided example might be a simplification or a slight variation. Let's stick to the problem's explicit example.

- If the prices of the stock in the last four days were `[7, 34, 1, 2]` and the price of the stock today is `8`, then the span for today is `3`. This is because, starting from today, the prices `[8, 2, 1]` (reading backward) were all less than or equal to `8`. The price `34` breaks the condition.

---

## Class Implementation

Implement the `StockSpanner` class:

### `StockSpanner()`

- Initializes the object of the class.

### `int next(int price)`

- Returns the span of the stock's price, given that today's price is `price`.

---

## Example 1

```
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[],,,,,,,]

Output:
[null, 1, 1, 1, 2, 1, 4, 6]
```

### Explanation:

```python
StockSpanner stockSpanner = new StockSpanner();

stockSpanner.next(100); // Returns 1 (Only 100 <= 100)
stockSpanner.next(80);  // Returns 1 (Only 80 <= 80)
stockSpanner.next(60);  // Returns 1 (Only 60 <= 60)
stockSpanner.next(70);  // Returns 2 (Because 70 <= 70 and 60 <= 70. Sequence:)
stockSpanner.next(60);  // Returns 1 (Only 60 <= 60)
stockSpanner.next(75);  // Returns 4 (Because 75 <= 75, 60 <= 75, 70 <= 75, 60 <= 75. Sequence:)
stockSpanner.next(85);  // Returns 6 (Because 85 <= 85, 75 <= 85, 60 <= 85, 70 <= 85, 60 <= 85, 80 <= 85. Sequence:)
```
## Constraints

- `1 <= price <= 10^5`
- At most `10^4` calls will be made to `next`.
```
