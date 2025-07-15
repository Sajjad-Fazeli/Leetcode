# Complexity Analysis
## Time Complexity:
Amortized `O(1)` for each call to next(). While there is a while loop, each element is pushed onto the stack exactly once. It can only be popped once. Therefore, over N calls to next(), there are at most N pushes and N pops in total. This averages out to a constant time complexity for each call.
## Space Complexity: 
`O(N)` in the worst case, where N is the number of calls made. If the prices are in strictly decreasing order (e.g., [100, 90, 80, ...]), the stack will store an entry for every price.
