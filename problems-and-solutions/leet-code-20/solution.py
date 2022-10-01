from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = deque()

        for bracket in s:
            if brackets.get(bracket):
                stack.append(bracket)
                continue
            
            if not len(stack):
                return False

            last_element = stack.pop()
            if last_element and brackets.get(last_element) != bracket:
                stack.append(last_element)
                return False

        return not len(stack) and True


if __name__  == "__main__":
    s = Solution()
    print(s.isValid("}"))
            
