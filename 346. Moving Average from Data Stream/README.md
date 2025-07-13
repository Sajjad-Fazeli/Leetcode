
# Moving Average from Data Stream

Given a stream of integers and a window size, your task is to calculate the moving average of all integers within the sliding window.

---

## Class Implementation

Implement the `MovingAverage` class with the following methods:

### `MovingAverage(int size)`

- Initializes the object with the specified `size` for the sliding window.

### `double next(int val)`

- Adds a new integer `val` to the stream.
- Returns the moving average of the last `size` values currently in the window.

---

## Example 1

```
Input:
["MovingAverage", "next", "next", "next", "next"]
[,,,,]

Output:
[null, 1.0, 5.5, 4.66667, 6.0]
```

### Explanation:

```java
MovingAverage movingAverage = new MovingAverage(3); // Window size is 3

movingAverage.next(1);   // Stream:
                         // Return: 1.0 (1 / 1)

movingAverage.next(10);  // Stream:
                         // Return: 5.5 ((1 + 10) / 2)

movingAverage.next(3);   // Stream: (window is full)
                         // Return: 4.66667 ((1 + 10 + 3) / 3)

movingAverage.next(5);   // Stream: (1 is pushed out, 5 is added)
                         // Return: 6.0 ((10 + 3 + 5) / 3)
```

---

## Constraints

- `1 <= size <= 1000`
- `-10^5 <= val <= 10^5`
- At most `10^4` calls will be made to `next`.
```
