class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []
        for s in components:
            if s == '.' or s == '':
                continue
            elif s == '..':
                    if stack:
                        stack.pop()
            else:
                    stack.append(s)
        if not stack:
            return '/'
        else:
            return "/" + "/".join(stack)   
