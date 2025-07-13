from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum value in a sliding window of size k.

    This solution uses a monotonic decreasing deque to achieve O(n) time complexity.
    The deque stores indices of elements, ensuring that the values at these indices
    are in decreasing order.
    """
    if not nums or k == 0:
        return []
    if k == 1:
        return nums

    result = []
    # The deque will store indices.
    dq = deque()

    for i, n in enumerate(nums):
        # 1. Remove indices from the back of the deque if the corresponding
        #    numbers are smaller than the current number. This maintains the
        #    decreasing order.
        while dq and nums[dq[-1]] < n:
            dq.pop()

        # 2. Add the current index to the back of the deque.
        dq.append(i)

        # 3. Remove the index from the front if it's out of the window's bounds.
        #    The window is of size k, so if the leftmost index is i-k, it's
        #    no longer in the current window [i-k+1, i].
        if dq[0] == i - k:
            dq.popleft()

        # 4. If the window is full (we have processed at least k elements),
        #    the maximum is at the front of the deque.
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
