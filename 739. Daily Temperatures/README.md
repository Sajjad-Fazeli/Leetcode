
# Daily Temperatures

Given an array of integers `temperatures` representing the daily temperatures, your task is to return an array `answer`.

For each day `i`, `answer[i]` should be the number of days you have to wait after the `i`th day to experience a warmer temperature. If there is no future day with a warmer temperature, then `answer[i]` should be `0`.

---

## Examples

### Example 1:
```
Input: temperatures =[73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

```

### Example 2:
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3:
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

---

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
