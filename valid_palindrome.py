'''125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lo, hi = 0, len(s)-1
        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
            elif not s[hi].isalnum():
                hi -= 1
            elif s[lo] != s[hi]:
                return False
            else:
                lo += 1
                hi -= 1
        return True

