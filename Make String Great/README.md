# Make String Good

Given a string `s` consisting of lower and upper case English letters.

A **good string** is defined as a string where there are **no two adjacent characters** `s[i]` and `s[i + 1]` such that:

- `0 <= i <= s.length - 2`
- `s[i]` is a lowercase letter and `s[i + 1]` is the same letter but in uppercase, **or**
- `s[i]` is an uppercase letter and `s[i + 1]` is the same letter but in lowercase.

---

## Task

To make the string good, repeatedly remove **adjacent pairs** of characters that violate the above rule (i.e., a lowercase and uppercase version of the same letter adjacent to each other).

You can continue removing such pairs as long as they exist.

Return the string after it has been made good.

---

## Notes

- The answer is guaranteed to be unique under the given constraints.
- An **empty string** is also considered good.

---

## Example

Input: `"leEeetcode"`  
Output: `"leetcode"`  

Explanation:  
- The substring `"eE"` is an adjacent lowercase and uppercase pair and is removed.
- Continuing this process once more yields the result `"leetcode"`.

