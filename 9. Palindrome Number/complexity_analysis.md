## Complexity Analysis

Let $$D$$ be the number of digits in the integer $$x$$. Note that $$D$$ is approximately $$\log_{10} |x|$$.

*   **Time Complexity:** $$O(\log_{10} |x|)$$ or $$O(D)$$
    *   The most efficient approach, especially considering the "follow-up" without string conversion, involves reversing half of the number. We repeatedly extract the last digit and build a reversed number until the original number becomes smaller than or equal to the reversed number.
    *   In each step, we perform constant-time operations (modulo and division). The number of steps is proportional to the number of digits in $$x$$ (specifically, about half the number of digits). Therefore, the time complexity is logarithmic with respect to the magnitude of $$x$$.

*   **Space Complexity:** $$O(1)$$
    *   When solving this problem without converting the integer to a string, we only use a few extra variables to store the reversed number and temporary values. The amount of extra space required does not depend on the magnitude of the input integer $$x$$.
