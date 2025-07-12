Let `n` be the length of the input string `s`.

Time complexity: `O(n)`

We only need one iteration over s.
At each step, we either remove the last character from stack, or add a character to stack, both of which take constant time.
Therefore, the overall time complexity is `O(n)`.
Space complexity: `O(n)`

We use a stack to store all the characters we encounter. Since we only pop characters when finding a pair, in worst-case scenario, we may have O(n) characters stored in stack. Thus the space complexity is `O(n)`.
