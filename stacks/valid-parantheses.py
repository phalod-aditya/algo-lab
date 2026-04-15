# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        # quick checks
        if s[0] ==')' or s[0] == '}' or s[0] == ']' or len(s) == 1:
            return False

        for i in s:

            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                # print(stack)

            elif i == ')' or i == ']' or i == '}':
                
                if not stack:
                    return False

                top = stack[-1]

                if ((i == ')' and top !='(') or (i == ']' and top !='[') or (i == '}' and top !='{')):
                    return False

                stack.pop()
                           
        return not stack
