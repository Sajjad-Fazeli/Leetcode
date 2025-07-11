
# Simplify Unix-style File Path

You are given an absolute path for a Unix-style file system, which always begins with a slash `/`. Your task is to transform this absolute path into its simplified canonical path.

---

## Rules of a Unix-style file system:

- A single period `.` represents the current directory.
- A double period `..` represents the previous/parent directory.
- Multiple consecutive slashes such as `//` and `///` are treated as a single slash `/`.
- Any sequence of periods that does not match the above should be treated as a valid directory or file name (e.g., `...` and `....`).

---

## Simplified canonical path requirements:

- The path must start with a single slash `/`.
- Directories within the path must be separated by exactly one slash `/`.
- The path must **not** end with a slash `/`, unless it is the root directory.
- The path must not contain any `.` or `..` used to denote the current or parent directory.

---

## Examples

### Example 1:
```
Input: path = "/home/"  
Output: "/home"  

Explanation:  
The trailing slash should be removed.
```

### Example 2:
```
Input: path = "/home//foo/"  
Output: "/home/foo"  

Explanation:  
Multiple consecutive slashes are replaced by a single slash.
```

### Example 3:
```
Input: path = "/home/user/Documents/../Pictures"  
Output: "/home/user/Pictures"  

Explanation:  
A double period `..` moves one directory up.
```

### Example 4:
```
Input: path = "/../"  
Output: "/"  

Explanation:  
Attempting to go above the root directory keeps you at root.
```

### Example 5:
```
Input: path = "/.../a/../b/c/../d/./"  
Output: "/.../b/d"  

Explanation:  
`...` is treated as a valid directory name.
```

---

## Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `.`, slash `/`, or underscore `_`.
- `path` is a valid absolute Unix path.

