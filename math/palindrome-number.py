# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:

        result = False
        str_x = ""

        str_x = str(x)
        # print(str_x)
        right = str_x[::-1]
        # print(right)

        if str_x == right:
            return True

        return result
