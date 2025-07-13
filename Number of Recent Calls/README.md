
# Recent Counter

You are tasked with implementing a `RecentCounter` class that counts the number of recent requests within a specific time frame.

---

## Class Implementation

Implement the `RecentCounter` class with the following methods:

### `RecentCounter()`

- Initializes the counter with zero recent requests.

### `int ping(int t)`

- **Adds a new request at time `t`**: `t` represents some time in milliseconds.
- **Returns the number of requests**: Specifically, it returns the count of requests that have occurred in the inclusive time range `[t - 3000, t]`. This range includes the newly added request at time `t`.

---

## Important Guarantee

- It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

---

## Example 1

```
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[],,,,]

Output:
[null, 1, 2, 3, 3]
```

### Explanation:

```python
RecentCounter recentCounter = new RecentCounter();

recentCounter.ping(1);     # requests =, range is [-2999, 1], returns 1
recentCounter.ping(100);   # requests =, range is [-2900, 100], returns 2
recentCounter.ping(3001);  # requests =, range is, returns 3
recentCounter.ping(3002);  # requests =, range is, returns 3
```

---

## Constraints

- `1 <= t <= 10^9`
- Each test case will call `ping` with strictly increasing values of `t`.
- At most `10^4` calls will be made to `ping`.
