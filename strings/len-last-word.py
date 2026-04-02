# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        final_len = 0

        # normalize whitespaces
        s = s.strip(' ')

        for char in s[::-1]:
            
            if char is ' ':
                break

            final_len += 1

        return final_len
